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
    telefono_fijo=models.CharField(max_length=9, verbose_name = "Teléfono fijo")    
    contacto = models.CharField(max_length=128)
    telefono_contacto=models.CharField(max_length=9, verbose_name = "Teléfono fijo")    
    estado= models.IntegerField(default=1)

    fecha_creacion= models.DateField(auto_now_add=True)
    usuario_creador=models.ForeignKey(User, related_name='pro_usuario_creador')
    fecha_modificacion= models.DateField(default=datetime.now())
    usuario_modificador=models.ForeignKey(User, related_name='pro_usuario_modificador')


    def __unicode__(self):  
        return u'%s' % (self.nombre)

class Beneficios(models.Model):
    nombre = models.CharField(max_length=128)    
    estado= models.IntegerField(default=1)

    fecha_creacion= models.DateField(auto_now_add=True)
    usuario_creador=models.ForeignKey(User, related_name='ben_usuario_creador')
    fecha_modificacion= models.DateField(default=datetime.now())
    usuario_modificador=models.ForeignKey(User, related_name='ben_usuario_modificador')

    def __unicode__(self):  
        return  u'%s' % (self.nombre)

class Alumno(models.Model):
    nombre = models.CharField(max_length=128)

    def __unicode__(self):  
        return self.nombre 

class Docente(models.Model):
    nombre = models.CharField(max_length=128)

    def __unicode__(self):  
        return self.nombre 

class CentroEducativo(models.Model):
    nombre = models.CharField(max_length=128)

    def __unicode__(self):  
        return self.nombre 

class Beneficio_Alumno(models.Model):
    beneficio= models.ForeignKey(Beneficios)
    alumno= models.ForeignKey(Alumno)
    estado= models.IntegerField(default=1)


    fecha_creacion= models.DateField(auto_now_add=True)
    usuario_creador=models.ForeignKey(User, related_name='ba_usuario_creador')
    fecha_modificacion= models.DateField(default=datetime.now())
    usuario_modificador=models.ForeignKey(User, related_name='ba_usuario_modificador')
    

    def __unicode__(self):  
        return u'%s' % (self.beneficio)

class Beneficio_Ce(models.Model):
    beneficio= models.ForeignKey(Beneficios)
    centro= models.ForeignKey(CentroEducativo)
    estado= models.IntegerField(default=1)

    fecha_creacion= models.DateField(auto_now_add=True)
    usuario_creador=models.ForeignKey(User, related_name='bce_usuario_creador')
    fecha_modificacion= models.DateField(default=datetime.now())
    usuario_modificador=models.ForeignKey(User, related_name='bce_usuario_modificador')
    

    def __unicode__(self):  
        return u'%s' % (self.beneficio)

class Beneficio_Docente(models.Model):
    beneficio= models.ForeignKey(Beneficios)
    docente= models.ForeignKey(Docente)
    estado= models.IntegerField(default=1)

    fecha_creacion= models.DateField(auto_now_add=True)
    usuario_creador=models.ForeignKey(User, related_name='bd_usuario_creador')
    fecha_modificacion= models.DateField(default=datetime.now())
    usuario_modificador=models.ForeignKey(User, related_name='bd_usuario_modificador')
    

    def __unicode__(self):  
        return u'%s' % (self.beneficio)


class Historico_Alumno(models.Model):
    beneficio= models.ForeignKey(Beneficios)
    descripcion= models.CharField(max_length=256)    
    alumno= models.ForeignKey(Alumno)
    proveedor= models.ForeignKey(Proveedor)
    cantidad= models.IntegerField(default=1)
    nombre_encargado= models.CharField(max_length=128)
    #telefono_encargado=models.CharField(max_length=9, verbose_name = "Teléfono fijo")    

    fecha_creacion= models.DateField(auto_now_add=True)
    fecha_modificacion= models.DateField(default=datetime.now())
    usuario_modificador=models.ForeignKey(User, related_name='ha_usuario_modificador')
    usuario_creador=models.ForeignKey(User, related_name='ha_usuario_creador')
    
    def __unicode__(self):  
        return u'%s' % (self.beneficio) 

class Historico_Docente(models.Model):
    beneficio= models.ForeignKey(Beneficios)
    descripcion= models.CharField(max_length=256)    
    docente= models.ForeignKey(Docente)
    proveedor= models.ForeignKey(Proveedor)
    cantidad= models.IntegerField(default=1)
    nombre_encargado= models.CharField(max_length=128)
    #telefono_encargado=models.CharField(max_length=9, verbose_name = "Teléfono fijo")    

    fecha_creacion= models.DateField(auto_now_add=True)
    fecha_modificacion= models.DateField(default=datetime.now())
    usuario_modificador=models.ForeignKey(User, related_name='hd_usuario_modificador')
    usuario_creador=models.ForeignKey(User, related_name='hd_usuario_creador')    

    def __unicode__(self):  
        return u'%s' % (self.beneficio)

class Historico_Centro(models.Model):
    beneficio= models.ForeignKey(Beneficios)
    descripcion= models.CharField(max_length=256)    
    centro= models.ForeignKey(CentroEducativo)
    proveedor= models.ForeignKey(Proveedor)
    cantidad= models.IntegerField(default=1)
    nombre_encargado= models.CharField(max_length=128)
    #telefono_encargado=models.CharField(max_length=9, verbose_name = "Teléfono fijo")    

    fecha_creacion= models.DateField(auto_now_add=True)
    fecha_modificacion= models.DateField(default=datetime.now())
    usuario_modificador=models.ForeignKey(User, related_name='hc_usuario_modificador')
    usuario_creador=models.ForeignKey(User, related_name='hc_usuario_creador')    

    def __unicode__(self):  
        return u'%s' % (self.beneficio)

