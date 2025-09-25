from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistroUsuarioForm, LoginForm, VacanteForm
from .models import Usuario


def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
                        #Por qué commit=false
            user = form.save(commit=False)
                        #por que form.cleaned_data, para que sirve ese metodo de form
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
        else:
            form = RegistroUsuarioForm()
        return render(request, 'registro.hmtl', {'form': form})
    
    
def iniciar_sesion(request):
    if request.method == 'POST':
        form =LoginForm(request.POST)
        if form.is_valid():
            documento = form.cleaned_data['documento']
            password = form.cleaned_data['password']
            try:
                            #explicar todo este bloque de codigo
                user_obj = Usuario.objects.get(documento=documento)
                user = authenticate(request, username=user_obj.email, password=password)
                if user is not None:
                    login(request, user)
                    if user.rol == 'empresa':
                        return redirect('crear_vacante')
                    else:
                        return redirect('home')
                else:
                    form.add_error(None, 'Documento o contraseña incorrectos.')
            except Usuario.DoesNotExist:
                form.add_error(None, 'Documento o contraseña incorrectos.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


from django.contrib.auth.decorators import login_required


@login_required
def crear_vacante(request):
    if request.user.rol != 'empresa':
        return redirect('home')
    
    if request.method == 'POST':
        form = VacanteForm(request.POST)
        if form.is_valid():
                        #por qué commit false
            vacante = form.save(commit=False)
            vacante.creador = request.user
            vacante.save()
            return redirect('home')
    else:
        form = VacanteForm()
    return render(request, 'crear_vacante.html', {'form': form})
    
def home(request):
    return render(request, 'home.html')