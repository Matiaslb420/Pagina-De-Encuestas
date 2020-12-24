from django.shortcuts import render, HttpResponse, redirect
from inicio.models import Encuesta, Puntajes
from random import choice
import clave


def inicio(request):
    return render(request, 'inicio.html')

def crear_encuesta_rapida(request):

    return render(request, 'crear_encuesta_rapida.html')
#Falta hacer que verifique el campo del titulo y las respuestas
def guardar_encuesta(request):
    if request.method == 'POST':
        opciones = {
            'respuesta1': request.POST['respuesta1'],
            'respuesta2': request.POST['respuesta2']
        }
        cantidad = 3
        respuesta = verificar_respuesta(request.POST,cantidad)
        while cantidad < 11:
            opciones[f'respuesta{str(cantidad)}'] = respuesta
            cantidad+=1
            respuesta = verificar_respuesta(request.POST, cantidad)
            existe_codigo = True
            while existe_codigo:
                codigo = clave.codigo()
                try:
                    Encuesta.objects.get(clave = codigo)
                except:
                    existe_codigo = False
 
            
        encuesta_creada = Encuesta(
            clave = codigo,
            titulo = request.POST['title'],
            res_1 = opciones['respuesta1'],
            res_2 = opciones['respuesta2'],
            res_3 = opciones['respuesta3'],
            res_4 = opciones['respuesta4'],
            res_5 = opciones['respuesta5'],
            res_6 = opciones['respuesta6'],
            res_7 = opciones['respuesta7'],
            res_8 = opciones['respuesta8'],
            res_9 = opciones['respuesta9'],
            res_10 = opciones['respuesta10'],
            autor = request.META['USERDOMAIN'],
            abierto = True
            )
        encuesta_creada.save()
        votos = Puntajes(
            clave = Encuesta.objects.get(clave = codigo),
            votos_1 = 0,
            votos_2 = 0,
            votos_3 = 0,
            votos_4 = 0,
            votos_5 = 0,
            votos_6 = 0,
            votos_7 = 0,
            votos_8 = 0,
            votos_9 = 0,
            votos_10 = 0
            )
        votos.save()
    return redirect('visualizacion', id= codigo)

def ver_encuesta(request, id):
    encuesta = Encuesta.objects.get(clave = id)
    votos = Puntajes.objects.get(clave = id)
    
    return render(request, 'encuesta_vista.html', {
        'titulo': encuesta.titulo,
        'respuesta':[
            encuesta.res_1,
            encuesta.res_2,
            encuesta.res_3,
            encuesta.res_4,
            encuesta.res_5,
            encuesta.res_6,
            encuesta.res_7,
            encuesta.res_8,
            encuesta.res_9,
            encuesta.res_10
            ],
        'puntaje':[
            votos.votos_1,
            votos.votos_2,
            votos.votos_3,
            votos.votos_4,
            votos.votos_5,
            votos.votos_6,
            votos.votos_7,
            votos.votos_8,
            votos.votos_9,
            votos.votos_10,
            ]
        }
    )


def verificar_respuesta(ultima_respuesta, cantidad):
    try:
        respuesta = ultima_respuesta[f'respuesta{cantidad}']
    except:
        respuesta = ''
    return respuesta

