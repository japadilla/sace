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
from django.db.models import Count


def IndexBeneficios(request):
	return render_to_response('beneficios/IndexBeneficios.html', context_instance=RequestContext(request))

def mapa(request):
	ctx={}
	beneficios= Beneficios.objects.all().annotate(count=Count('pk'))	
	centro= CentroEducativo.objects.all()
	ctx['beneficios']=beneficios.count()
	ctx['centro']=centro
	print beneficios.count()
	return render_to_response('beneficios/mapa.html',ctx, context_instance=RequestContext(request))


def reportes(request):
	
	return render_to_response('beneficios/Reportes.html', context_instance=RequestContext(request))

def MostrarBeneficios(request):
	if request.method =='GET':
		ctx={}
		beneficios= Beneficios.objects.all()
		ctx['beneficios']=beneficios
		return render_to_response('beneficios/Beneficios.html', ctx, context_instance=RequestContext(request))
	elif request.method == 'POST':
		ctx={}
		buscar=request.POST['buscar'].strip()
		beneficios= Beneficios.objects.filter(Q(nombre__icontains=buscar))
		ctx['beneficios']=beneficios
	return render_to_response('beneficios/Beneficios.html', ctx, context_instance=RequestContext(request))

def MostrarBeneficioCE(request):
	if request.method =='GET':
		ctx={}
		beneficiosCentro= Beneficio_Ce.objects.filter(Q(estado=1))
		proveedor= Proveedor.objects.all()
		beneficios= Beneficios.objects.all()
		historico= Historico_Centro.objects.all()
		beneficiado= CentroEducativo.objects.all()
		ctx['proveedor']=proveedor		
		ctx['beneficiado']=beneficiado
		ctx['beneficios']=beneficios
		ctx['beneficiosCentro']=beneficiosCentro			
		ctx['historico']=historico
		return render_to_response('beneficios/Mostrar_Beneficios_Centro.html', ctx, context_instance=RequestContext(request))
	elif request.method == 'POST':
		ctx={}
		buscar=request.POST['buscar'].strip()
		beneficios= Beneficios.objects.all()
		historico= Historico_Centro.objects.all()
		beneficiosCentro= Beneficio_Ce.objects.filter(Q(nombre__icontains=buscar), Q(estado=1))
		proveedor= Proveedor.objects.all()
		beneficiado= CentroEducativo.objects.all()
		print eliminar
		ctx['proveedor']=proveedor		
		ctx['beneficiado']=beneficiado
		ctx['beneficios']=beneficios
		ctx['beneficiosCentro']=beneficiosCentro
		ctx['historico']=historico
	return render_to_response('beneficios/Mostrar_Beneficios_Centro.html', ctx, context_instance=RequestContext(request))

def MostrarBeneficioAlumno(request):
	if request.method =='GET':
		ctx={}
		beneficio= Beneficio_Alumno.objects.filter(Q(estado=1))
		proveedor= Proveedor.objects.all()
		beneficios= Beneficios.objects.all()
		beneficiado= Alumno.objects.all()
		historico= Historico_Alumno.objects.all()
		ctx['proveedor']=proveedor		
		ctx['beneficiado']=beneficiado
		ctx['beneficios']=beneficios
		ctx['beneficio']=beneficio	
		ctx['historico']=historico	
		return render_to_response('beneficios/Mostrar_Beneficios_Alumno.html', ctx, context_instance=RequestContext(request))
	elif request.method == 'POST':
		ctx={}
		buscar=request.POST['buscar'].strip()
		beneficios= Beneficios.objects.all()
		beneficio= Beneficio_Alumno.objects.filter(Q(nombre__icontains=buscar), Q(estado=1))
		proveedor= Proveedor.objects.all()
		historico= Historico_Alumno.objects.all()
		beneficiado= Alumno.objects.all()
		print eliminar
		ctx['proveedor']=proveedor		
		ctx['beneficiado']=beneficiado
		ctx['beneficios']=beneficios
		ctx['beneficio']=beneficio
		ctx['historico']=historico	
	return render_to_response('beneficios/Mostrar_Beneficios_Alumno.html', ctx, context_instance=RequestContext(request))

def MostrarBeneficioDocente(request):
	if request.method =='GET':
		ctx={}
		beneficiod= Beneficio_Docente.objects.filter(Q(estado=1))
		proveedor= Proveedor.objects.all()
		beneficios= Beneficios.objects.all()
		beneficiado= Docente.objects.all()
		historico= Historico_Docente.objects.all()
		ctx['proveedor']=proveedor		
		ctx['beneficiado']=beneficiado
		ctx['beneficios']=beneficios
		ctx['beneficiod']=beneficiod
		ctx['historico']=historico		
		return render_to_response('beneficios/Mostrar_Beneficios_Docente.html', ctx, context_instance=RequestContext(request))
	elif request.method == 'POST':
		ctx={}
		buscar=request.POST['buscar'].strip()
		beneficios= Beneficios.objects.all()
		beneficiod= Beneficio_Docente.objects.filter(Q(nombre__icontains=buscar), Q(estado=1))
		proveedor= Proveedor.objects.all()
		beneficiado= Docente.objects.all()
		historico= Historico_Docente.objects.all()
		print eliminar
		ctx['proveedor']=proveedor		
		ctx['beneficiado']=beneficiado
		ctx['beneficios']=beneficios
		ctx['beneficiod']=beneficiod
		ctx['historico']=historico
	return render_to_response('beneficios/Mostrar_Beneficios_Docente.html', ctx, context_instance=RequestContext(request))

	
def MostrarProveedores(request):
	if request.method =='GET':
		ctx={}
		proveedor= Proveedor.objects.all()
		ctx['proveedor']=proveedor
		return render_to_response('beneficios/proveedores.html', ctx, context_instance=RequestContext(request))
	elif request.method == 'POST':
		ctx={}
		buscar=request.POST['buscar'].strip()
		proveedor= Proveedor.objects.filter(Q(nombre__icontains=buscar) | Q(telefono_fijo__icontains=buscar))
		ctx['proveedor']=proveedor
	return render_to_response('beneficios/proveedores.html', ctx, context_instance=RequestContext(request))

def editarBeneficio(request, beneficio_id):
	if request.method =='GET':
		ctx={}
		beneficio= Beneficios.objects.get(pk=beneficio_id)
		titulo="Editar Beneficio"
		mensaje="Seleccione los valores para editar el beneficio social."
		ctx['beneficio']= beneficio		
		ctx['titulo']= titulo
		ctx['mensaje']= mensaje		
	 	return render_to_response('beneficios/AgregarBeneficio.html', ctx, context_instance=RequestContext(request))
	elif request.method == 'POST':	
		beneficio = request.POST['beneficio'].strip()
        cuenta= request.POST['id']        
    	beneficio1= Beneficios(id= cuenta, nombre=beneficio,fecha_creacion=datetime.now(), usuario_creador_id=1,fecha_modificacion=datetime.now(), usuario_modificador_id=1)
	beneficio1.save()
	return HttpResponseRedirect(reverse('MostrarBeneficios'))

def eliminarBeneficio(request, beneficio_id):
	beneficio= Beneficios.objects.filter(pk=beneficio_id).delete()
	return HttpResponseRedirect(reverse('MostrarBeneficios'))

def DesactivarBeneficioCe(request, beneficio_id):
	beneficio= Beneficio_Ce.objects.filter(id=beneficio_id).update(estado=0)
	return HttpResponseRedirect(reverse('MostrarBeneficioCE'))

def DesactivarBeneficioAlumno(request, beneficio_id):
	beneficio= Beneficio_Alumno.objects.filter(id=beneficio_id).update(estado=0)
	return HttpResponseRedirect(reverse('MostrarBeneficioAlumno'))

def DesactivarBeneficioDocente(request, beneficio_id):
	beneficio= Beneficio_Docente.objects.filter(id=beneficio_id).update(estado=0)
	return HttpResponseRedirect(reverse('MostrarBeneficioDocente'))


def eliminarProveedor(request, proveedor_id):
	proveedor= Proveedor.objects.filter(pk=proveedor_id).delete()
	return HttpResponseRedirect(reverse('MostrarProveedores'))

def editarProveedor(request, proveedor_id):
	if request.method =='GET':
		ctx={}
		proveedor= Proveedor.objects.get(pk=proveedor_id)
		ctx['proveedor']=proveedor
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
		proveedor= Proveedor.objects.all()
		titulo="Crear Un Nuevo Beneficio"
		mensaje="Ingrese los siguientes valores para la creación de un nuevo beneficio social."
		ctx['proveedor']=proveedor
		ctx['titulo']= titulo
		ctx['mensaje']= mensaje
	 	return render_to_response('beneficios/AgregarBeneficio.html', ctx, context_instance=RequestContext(request))
	elif request.method == 'POST':	
		ctx={}
		beneficio = request.POST['beneficio'].strip()
        insert= Beneficios(nombre=beneficio, fecha_creacion=datetime.now(),usuario_modificador_id=1, fecha_modificacion=datetime.now(),usuario_creador_id=1,)
        insert.save()
	return HttpResponseRedirect(reverse('MostrarBeneficios'))

def BeneficioCe(request):
	if request.method =='GET':
		ctx={}
		beneficio= Beneficios.objects.all()
		centro= CentroEducativo.objects.all()
		proveedor= Proveedor.objects.all()
		ctx['centro']=centro
		ctx['beneficio']= beneficio
		ctx['proveedor']= proveedor
		return render_to_response('beneficios/Beneficio_Centro.html', ctx,context_instance=RequestContext(request))
	elif request.method == 'POST':
		ctx={}
		beneficio= request.POST['beneficio'].strip()
		proveedor= request.POST['proveedor'].strip()
		descripcion= request.POST['descripcion'].strip()
		beneficiado= request.POST['beneficiado'].strip()
		cantidad= request.POST['cantidad'].strip()
		encargado= request.POST['encargado'].strip()
		insert1= Historico_Centro(beneficio_id=beneficio,
								descripcion=descripcion,
								centro_id= beneficiado,
								proveedor_id= proveedor,
								nombre_encargado= encargado,
								cantidad= cantidad,
								usuario_modificador_id=1,
								fecha_modificacion=datetime.now(),
								usuario_creador_id=1,)
		insert2= Beneficio_Ce(beneficio_id=beneficio,								
								centro_id= beneficiado,								
								usuario_modificador_id=1,
								fecha_modificacion=datetime.now(),
								usuario_creador_id=1,)
        insert1.save()
        insert2.save()
	return HttpResponseRedirect(reverse('MostrarBeneficioCE'))


def BeneficioAlumno(request):
	if request.method =='GET':
		ctx={}
		beneficio= Beneficios.objects.all()
		alumno= Alumno.objects.all()
		proveedor= Proveedor.objects.all()
		ctx['alumno']=alumno
		ctx['beneficio']= beneficio
		ctx['proveedor']= proveedor
		return render_to_response('beneficios/Nuevo_Beneficio_Alumno.html', ctx,context_instance=RequestContext(request))
	elif request.method == 'POST':
		beneficio= request.POST['beneficio'].strip()
		proveedor= request.POST['proveedor'].strip()
		descripcion= request.POST['descripcion'].strip()
		beneficiado= request.POST['beneficiado'].strip()
		cantidad= request.POST['cantidad'].strip()
		encargado= request.POST['encargado'].strip()
		insert1= Historico_Alumno(beneficio_id=beneficio,
								descripcion=descripcion,
								alumno_id= beneficiado,
								proveedor_id= proveedor,
								nombre_encargado= encargado,
								cantidad= cantidad,
								usuario_modificador_id=1,
								fecha_modificacion=datetime.now(),
								usuario_creador_id=1,)
		insert2= Beneficio_Alumno(beneficio_id=beneficio,								
								alumno_id= beneficiado,								
								usuario_modificador_id=1,
								fecha_modificacion=datetime.now(),
								usuario_creador_id=1,)
        insert1.save()
        insert2.save()
	return HttpResponseRedirect(reverse('MostrarBeneficioAlumno'))

def BeneficioDocente(request):
	if request.method =='GET':
		ctx={}
		beneficio= Beneficios.objects.all()
		docente= Docente.objects.all()
		proveedor= Proveedor.objects.all()
		ctx['docente']=docente
		ctx['beneficio']= beneficio
		ctx['proveedor']= proveedor
		return render_to_response('beneficios/Nuevo_Beneficio_Docente.html', ctx,context_instance=RequestContext(request))
	elif request.method == 'POST':
		ctx={}
		beneficio= request.POST['beneficio'].strip()
		proveedor= request.POST['proveedor'].strip() 
		descripcion= request.POST['descripcion'].strip()
		beneficiado= request.POST['beneficiado'].strip()
		cantidad= request.POST['cantidad'].strip()
		encargado= request.POST['encargado'].strip()
		insert1= Historico_Docente(beneficio_id=beneficio,
								descripcion=descripcion,
								docente_id= beneficiado,
								proveedor_id= proveedor,
								nombre_encargado= encargado,
								cantidad= cantidad,
								usuario_modificador_id=1,
								fecha_modificacion=datetime.now(),
								usuario_creador_id=1,)
        insert2= Beneficio_Docente(beneficio_id=beneficio,								
								docente_id= beneficiado,								
								usuario_modificador_id=1,
								fecha_modificacion=datetime.now(),
								usuario_creador_id=1,)
        insert1.save()
        insert2.save()
	return HttpResponseRedirect(reverse('MostrarBeneficioDocente'))



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


