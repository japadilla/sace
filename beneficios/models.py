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
    cantidad= models.IntegerField(default=1)
    fecha_creacion= models.DateField(default=datetime.now())
    usuario_creador=models.ForeignKey(User, related_name='ben_usuario_creador')
    fecha_modificacion= models.DateField(default=datetime.now())
    usuario_modificador=models.ForeignKey(User, related_name='ben_usuario_modificador')
    estado= models.IntegerField(default=1)

    def __unicode__(self):  
        return self.nombre

class Alumno(models.Model):
    alumno= models.IntegerField()

    def __unicode__(self):  
        return self.alumno 

class Docente(models.Model):
    docente= models.IntegerField()

    def __unicode__(self):  
        return self.docente 

class CentroEducativo(models.Model):
    centro= models.IntegerField()

    def __unicode__(self):  
        return self.centro 

class Beneficio_Alumno(models.Model):
    beneficio= models.ForeignKey(Beneficios)
    alumno= models.ForeignKey(Alumno)
    fecha_creacion= models.DateField(default=datetime.now())
    usuario_creador=models.ForeignKey(User, related_name='ba_usuario_creador')
    fecha_modificacion= models.DateField(default=datetime.now())
    usuario_modificador=models.ForeignKey(User, related_name='ba_usuario_modificador')
    estado= models.IntegerField(default=1)

    def __unicode__(self):  
        return self.beneficio, self.alumno 

class Beneficio_Ce(models.Model):
    beneficio= models.ForeignKey(Beneficios)
    centro= models.ForeignKey(CentroEducativo)
    fecha_creacion= models.DateField(default=datetime.now())
    usuario_creador=models.ForeignKey(User, related_name='bce_usuario_creador')
    fecha_modificacion= models.DateField(default=datetime.now())
    usuario_modificador=models.ForeignKey(User, related_name='bce_usuario_modificador')
    estado= models.IntegerField(default=1)

    def __unicode__(self):  
        return self.beneficio, self.centro 

class Beneficio_Docente(models.Model):
    beneficio= models.ForeignKey(Beneficios)
    docente= models.ForeignKey(Docente)
    fecha_creacion= models.DateField(default=datetime.now())
    usuario_creador=models.ForeignKey(User, related_name='bd_usuario_creador')
    fecha_modificacion= models.DateField(default=datetime.now())
    usuario_modificador=models.ForeignKey(User, related_name='bd_usuario_modificador')
    estado= models.IntegerField(default=1)

    def __unicode__(self):  
        return self.beneficio, self.docente 


class Historico_Alumno(models.Model):
    beneficio= models.ForeignKey(Beneficios)
    alumno= models.ForeignKey(Alumno)
    proveedor= models.ForeignKey(Proveedor)
    cantidad= models.IntegerField(default=1)
    fecha_creacion= models.DateField(default=datetime.now())
    fecha_modificacion= models.DateField(default=datetime.now())
    usuario_modificador=models.ForeignKey(User, related_name='ha_usuario_modificador')
    usuario_creador=models.ForeignKey(User, related_name='ha_usuario_creador')
    usuario_encargado= models.ForeignKey(User, related_name='ha_encargado_recibir_beneficio')

    def __unicode__(self):  
        return self.beneficio, self.alumno, self.proveedor  

class Historico_Docente(models.Model):
    beneficio= models.ForeignKey(Beneficios)
    docente= models.ForeignKey(Docente)
    proveedor= models.ForeignKey(Proveedor)
    cantidad= models.IntegerField(default=1)
    fecha_creacion= models.DateField(default=datetime.now())
    fecha_modificacion= models.DateField(default=datetime.now())
    usuario_modificador=models.ForeignKey(User, related_name='hd_usuario_modificador')
    usuario_creador=models.ForeignKey(User, related_name='hd_usuario_creador')
    usuario_encargado= models.ForeignKey(User, related_name='hd_encargado_recibir_beneficio')

    def __unicode__(self):  
        return self.beneficio, self.docente, self.proveedor 

class Historico_Centro(models.Model):
    beneficio= models.ForeignKey(Beneficios)
    centro= models.ForeignKey(CentroEducativo)
    proveedor= models.ForeignKey(Proveedor)
    cantidad= models.IntegerField(default=1)
    fecha_creacion= models.DateField(default=datetime.now())
    fecha_modificacion= models.DateField(default=datetime.now())
    usuario_modificador=models.ForeignKey(User, related_name='hc_usuario_modificador')
    usuario_creador=models.ForeignKey(User, related_name='hc_usuario_creador')
    usuario_encargado= models.ForeignKey(User, related_name='hc_encargado_recibir_beneficio')

    def __unicode__(self):  
        return self.beneficio, self.centro, self.proveedor 

