from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import CrearUsuarioForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect('usuarios')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('usuarios')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def usuarios_view(request):
    if request.method == 'POST':
        form = CrearUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado correctamente.')
            return redirect('usuarios')
    else:
        form = CrearUsuarioForm()

    usuarios = User.objects.all().order_by('id')
    contexto = {
        'form': form,
        'usuarios': usuarios,
    }
    return render(request, 'usuarios.html', contexto)


@login_required
def eliminar_usuario(request, user_id):
    usuario = get_object_or_404(User, id=user_id)
    if request.user == usuario:
        messages.error(request, 'No puedes eliminar tu propio usuario.')
    else:
        usuario.delete()
        messages.success(request, 'Usuario eliminado correctamente.')
    return redirect('usuarios')


@login_required
def creditos_view(request):
    return render(request, 'creditos.html')
