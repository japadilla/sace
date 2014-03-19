# -*- encoding: utf-8 -*-
from datetime import datetime
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

class Proveedor(models.Model):
    nombre = models.CharField(max_length=128)
    direccion = models.CharField(max_length=512)
    telefono_fijo=models.CharField(max_length=8, verbose_name = "Teléfono fijo")
    fecha_creacion= models.DateField(default=datetime.now())
    usuario_creador=models.ForeignKey(User, related_name='pro_usuario_creador')
    fecha_modificacion= models.DateField(default=datetime.now())
    usuario_modificador=models.ForeignKey(User, related_name='pro_usuario_modificador')
    estado= models.IntegerField(default=1)


    def __unicode__(self):  
        return self.nombre

class Beneficios(models.Model):
    nombre = models.CharField(max_length=128)
    descripcion= models.CharField(max_length=256)
    fecha_creacion= models.DateField(default=datetime.now())
    usuario_creador=models.ForeignKey(User, related_name='ben_usuario_creador')
    fecha_modificacion= models.DateField(default=datetime.now())
    usuario_modificador=models.ForeignKey(User, related_name='ben_usuario_modificador')
    estado= models.IntegerField(default=1)

    def __unicode__(self):  
        return self.nombre    	



