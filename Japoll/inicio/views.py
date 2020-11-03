from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def crear_encuesta_rapida(request):

    return render(request, 'crear_encuesta_rapida.html')

