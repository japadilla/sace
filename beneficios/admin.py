from django.contrib import admin
from beneficios.models import *

class ProveedorAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'direccion', 'telefono_fijo')

class BeneficiosAdmin(admin.ModelAdmin):
	list_display= ('nombre', 'descripcion', 'fecha_creacion')
    
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Beneficios, BeneficiosAdmin)