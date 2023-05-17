from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate #creacion de una cookies para /darle restricciones, o veer quiene creo alguna tarea /o sesion que guarda informacion de usuario
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db import IntegrityError

# Create your views here.

def home(request):
    return render(request, 'home.html')


def register(request):

    if request.method == 'GET':
        return render(request, 'register.html',{
            'form': UserCreationForm
    })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.
                POST['password1'])
                user.save()
                return HttpResponse('Se creo el Usuario.')
            except:
                return render(request, 'register.html',{
                'form': UserCreationForm,
                'error': 'Usuario ya Existe.'
                })
        return render(request, 'register.html',{
            'form': UserCreationForm,
            'error': 'Contraseña no Coinciden.'
        })

def index(request):
    return render(request, 'index.html')

def iniciarS(request):
    if request.method == 'GET':
        return render(request, 'iniciarS.html', {
            "form": AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'iniciarS.html', {
            "form": AuthenticationForm, "error": "Usuario o contraseña Incorrecta."
        })

        login(request, user)
        return redirect('index')