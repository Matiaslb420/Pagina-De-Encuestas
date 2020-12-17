from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def crear_encuesta_rapida(request):

    return render(request, 'crear_encuesta_rapida.html')

def guardar_encuesta(request):
    if request.method == 'POST':
        Titulo = request.POST['title']
        opciones = {
            'respuesta1': request.POST['respuesta1'],
            'respuesta2': request.POST['respuesta2']
        }
        cantidad = 3
        respuesta = verificar_respuesta(request.POST,cantidad)
        while respuesta:
            opciones[f'respuesta{str(cantidad)}'] = respuesta
            cantidad+=1
            respuesta = verificar_respuesta(request.POST, cantidad)
    return HttpResponse('UwU')

def verificar_respuesta(ultima_respuesta, cantidad):
    try:
        respuesta = ultima_respuesta[f'respuesta{cantidad}']
    except:
        respuesta = False
    else:
        if len(respuesta) < 1:
            respuesta = False
    return respuesta

