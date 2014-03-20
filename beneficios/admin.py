from django.contrib import admin
from beneficios.models import *

class ProveedorAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'direccion', 'telefono_fijo')

class BeneficiosAdmin(admin.ModelAdmin):
	list_display= ('nombre', 'fecha_creacion')
    
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Beneficios, BeneficiosAdmin)
admin.site.register(Alumno)
admin.site.register(Docente)
admin.site.register(CentroEducativo)
admin.site.register(Beneficio_Alumno)
admin.site.register(Beneficio_Ce)
admin.site.register(Beneficio_Docente)
admin.site.register(Historico_Alumno)
admin.site.register(Historico_Docente)
admin.site.register(Historico_Centro)
