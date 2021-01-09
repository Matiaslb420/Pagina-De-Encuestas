from django.shortcuts import render, HttpResponse, redirect
from inicio.models import Encuesta, Puntajes, Votantes
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
            ],
        'clave': id,
        }
    )


def verificar_respuesta(ultima_respuesta, cantidad):
    try:
        respuesta = ultima_respuesta[f'respuesta{cantidad}']
    except:
        respuesta = ''
    return respuesta

def ver_grafica(request, id):
    encuesta = Encuesta.objects.get(clave = id)
    votos = Puntajes.objects.get(clave = id)
    #agregar que pasa si está cerrada
    if encuesta.abierto == False:
        pass
    return render(request, 'encuesta_grafica.html',{
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
            ],
        }
                  )
def votar(request):
    if request.method == 'POST':
        id, opcion = request.POST['respuesta'].split('-')
        voto = Puntajes.objects.get(clave = id)
        if opcion == '0':
            voto.votos_1 += 1
        elif opcion == '1':
            voto.votos_2 +=1
        elif opcion == '2':
            voto.votos_3 += 1
        elif opcion == '3':
            voto.votos_4 +=1
        elif opcion == '4':
            voto.votos_5 += 1
        elif opcion == '5':
            voto.votos_6 +=1
        elif opcion == '6':
            voto.votos_7 += 1
        elif opcion == '7':
            voto.votos_8 +=1
        elif opcion == '8':
            voto.votos_9 += 1
        elif opcion == '9':
            voto.votos_10 +=1
        else:
            print(opcion)
            print(voto.res_0)
        voto.save()
        return redirect('grafica', id = id)