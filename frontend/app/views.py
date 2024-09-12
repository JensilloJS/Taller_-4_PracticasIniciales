# my_django_app/views.py
from django.shortcuts import render, redirect
from .forms import LoginForm, RegistroForm
from django.http import JsonResponse
import requests
from django.http import HttpResponse
import json

def home(request):
    return render(request, 'login.html')

def login(request):
    return render(request, 'login.html')

def principal(request):
    user_id = request.COOKIES.get('user_id')
    if user_id:
        return render(request, 'PantallaInicial.html', {'user_id': user_id})
    else:
        return redirect('login')

from django.shortcuts import render, redirect
from django.http import JsonResponse
import requests

def signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = {
                'id': form.cleaned_data['id'],
                'password': form.cleaned_data['password']
            }
            # Petición POST al backend 
            try:
                response = requests.post('http://localhost:5000/login', json=data)
                response.raise_for_status()
                
                # Verifica el contenido de la respuesta
                respuesta = response.json()
                
                if response.status_code == 200:
                    # Redirige a la pagina pincipal
                    response = redirect('principal')  
                     # Guarda el user_id en una cookie
                    response.set_cookie('user_id', data['id']) 
                    return response
                else:
                    #
                    return JsonResponse({'message': respuesta.get('error', 'Login failed')}, status=response.status_code)
            except requests.exceptions.RequestException as e:
                return JsonResponse({'error': 'Error en la conexión con el servidor'}, status=500)
            except ValueError:
                return JsonResponse({'error': 'Error en la respuesta del servidor'}, status=500)
        else:
            return JsonResponse({'error': 'Datos del formulario inválidos'}, status=400)
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(f"Datos enviados al servidor: {data}")  # Verifica qué datos estás enviando
            response = requests.post('http://localhost:5000/registro', json=data)
            if response.status_code == 201:
                return redirect('login')  # Redirige a otra página en caso de éxito
            else:
                print(response.status_code)
                print(response.json())  # Verifica qué error está devolviendo el servidor
                return JsonResponse({'message': 'Registration failed'}, status=400)
    else:
        form = RegistroForm()
    return render(request, 'RegistroUsuario.html', {'form': form})

def ir_registro(request):
    return render(request, 'RegistroUsuario.html')
