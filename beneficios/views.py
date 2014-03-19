# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from beneficios.models import *
from django.core.urlresolvers import reverse
from django.http import Http404
from django.views import generic
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import * #Group, User
from django.contrib.auth import authenticate, login
from django.template.defaultfilters import stringfilter
from django.db.models import Q


def IndexBeneficios(request):
	return render_to_response('beneficios/IndexBeneficios.html', context_instance=RequestContext(request))

def MostrarBeneficios(request):
	if request.method =='GET':
		ctx={}
		b= Beneficios.objects.all()
		#p= Proveedor.objects.all()
		#ctx['proveedor']=p
		ctx['beneficios']=b
		return render_to_response('beneficios/Beneficios.html', ctx, context_instance=RequestContext(request))
	elif request.method == 'POST':
		ctx={}
		buscar=request.POST['buscar'].strip()
		b= Beneficios.objects.filter(Q(nombre__icontains=buscar) | Q(descripcion__icontains=buscar))
		#p= Proveedor.objects.all()
		#ctx['proveedor']=p
		ctx['beneficios']=b
		return render_to_response('beneficios/Beneficios.html', ctx, context_instance=RequestContext(request))
		ba:8b:31:4b:b8:2c:df:74:fb:19:fb:c6:e4:ae:3d:64 jose.padilla@se.gob.hn


def MostrarProveedores(request):
	if request.method =='GET':
		ctx={}
		p= Proveedor.objects.all()
		ctx['proveedor']=p
		return render_to_response('beneficios/proveedores.html', ctx, context_instance=RequestContext(request))
	elif request.method == 'POST':
		ctx={}
		buscar=request.POST['buscar'].strip()
		p= Proveedor.objects.filter(Q(nombre__icontains=buscar) | Q(telefono_fijo__icontains=buscar))
		ctx['proveedor']=p
	return render_to_response('beneficios/proveedores.html', ctx, context_instance=RequestContext(request))

def editarBeneficio(request, beneficio_id):
	if request.method =='GET':
		ctx={}
		beneficio= Beneficios.objects.get(pk=beneficio_id)
		#u= Proveedor.objects.all()
		titulo="Editar Beneficio"
		mensaje="Seleccione los valores para editar el beneficio social."
		#ctx['proveedor']=u
		ctx['beneficio']= beneficio		
		ctx['titulo']= titulo
		ctx['mensaje']= mensaje
		beneficio1= Beneficios(id= beneficio_id, nombre="prueba", descripcion="prueba", fecha_creacion=datetime.now(), usuario_creador_id=1,fecha_modificacion=datetime.now(), usuario_modificador_id=1)
	 	return render_to_response('beneficios/AgregarBeneficio.html', ctx, context_instance=RequestContext(request))
	elif request.method == 'POST':	
		beneficio = request.POST['beneficio'].strip()
        descripcion = request.POST['beneficioDsc'].strip()
        #proveedor = request.POST['proveedor'].strip()
        cuenta= request.POST['id']        
    	beneficio1= Beneficios(id= cuenta, nombre=beneficio, descripcion=descripcion, fecha_creacion=datetime.now(), usuario_creador_id=1,fecha_modificacion=datetime.now(), usuario_modificador_id=1)
	beneficio1.save()
	return HttpResponseRedirect(reverse('MostrarBeneficios'))

def eliminarBeneficio(request, beneficio_id):
	beneficio= Beneficios.objects.filter(pk=beneficio_id).delete()
	return HttpResponseRedirect(reverse('MostrarBeneficios'))

def eliminarProveedor(request, proveedor_id):
	proveedor= Proveedor.objects.filter(pk=proveedor_id).delete()
	return HttpResponseRedirect(reverse('MostrarProveedores'))

def editarProveedor(request, proveedor_id):
	if request.method =='GET':
		ctx={}
		u= Proveedor.objects.get(pk=proveedor_id)
		ctx['proveedor']=u
	 	return render_to_response('beneficios/AgregarProveedor.html', ctx, context_instance=RequestContext(request))
	elif request.method == 'POST':	
		proveedor = request.POST['proveedor'].strip()
        direccion = request.POST['direccion'].strip()
        telefono = request.POST['telefono'].strip()
        cuenta= request.POST['id']     
    	update=Proveedor(id=cuenta, nombre=proveedor, direccion=direccion, telefono_fijo= telefono, fecha_creacion=datetime.now(),usuario_creador_id=1, fecha_modificacion=datetime.now(),usuario_modificador_id=1)
        update.save()
	return HttpResponseRedirect(reverse('MostrarProveedores'))
	
def AgregarBeneficios(request):
	if request.method =='GET':
		ctx={}
		u= Proveedor.objects.all()
		titulo="Crear Un Nuevo Beneficio"
		mensaje="Ingrese los siguientes valores para la creación de un nuevo beneficio social."
		ctx['proveedor']=u
		ctx['titulo']= titulo
		ctx['mensaje']= mensaje
	 	return render_to_response('beneficios/AgregarBeneficio.html', ctx, context_instance=RequestContext(request))
	elif request.method == 'POST':	
		ctx={}
		beneficio = request.POST['beneficio'].strip()
        descripcion = request.POST['beneficioDsc'].strip()
        #proveedor = request.POST['proveedor'].strip()
        insert= Beneficios(nombre=beneficio, descripcion=descripcion, fecha_creacion=datetime.now(), usuario_modificador_id=1, fecha_modificacion=datetime.now(),usuario_creador_id=1,)
        insert.save()
	return HttpResponseRedirect(reverse('MostrarBeneficios'))

def BeneficioCe(request):
	ctx={}
	beneficio= Beneficios.objects.all()
	#u= Proveedor.objects.all()
	#ctx['proveedor']=u
	ctx['beneficio']= beneficio
	return render_to_response('beneficios/Beneficio_Centro.html', ctx,context_instance=RequestContext(request))

def AgregarProveedor(request):
	if request.method =='GET':
	 	return render_to_response('beneficios/AgregarProveedor.html', context_instance=RequestContext(request))
	elif request.method == 'POST':	
		ctx={}
		proveedor = request.POST['proveedor'].strip()
        direccion = request.POST['direccion'].strip()
        telefono = request.POST['telefono'].strip()
        insert=Proveedor(nombre=proveedor, direccion=direccion, telefono_fijo= telefono,fecha_creacion=datetime.now(), usuario_creador_id=1, fecha_modificacion=datetime.now(),usuario_modificador_id=1)
        insert.save()
	return HttpResponseRedirect(reverse('MostrarProveedores'))


