from django.db import models

# Create your models here.
class Encuesta(models.Model):
    clave = models.CharField(max_length=4,  unique = True, primary_key = True)
    titulo = models.CharField(max_length=40)
    res_1 = models.CharField(max_length=40)
    res_2 = models.CharField(max_length=40)
    res_3 = models.CharField(max_length=40, blank =True)
    res_4 = models.CharField(max_length=40, blank =True)
    res_5 = models.CharField(max_length=40, blank =True)
    res_6 = models.CharField(max_length=40, blank =True)
    res_7 = models.CharField(max_length=40, blank =True)
    res_8 = models.CharField(max_length=40, blank =True)
    res_9 = models.CharField(max_length=40, blank =True)
    res_10 = models.CharField(max_length=40, blank =True)
    autor = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    abierto = models.BooleanField()