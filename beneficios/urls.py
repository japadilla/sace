from django.conf.urls import patterns, url
from beneficios import views

urlpatterns = patterns('',
    url(r'^Beneficios/$', views.IndexBeneficios, name='IndexBeneficios'),
    url(r'^Beneficios/mapa/$', views.mapa, name='mapa'),
    url(r'^MostrarBeneficios/$', views.MostrarBeneficios, name='MostrarBeneficios'),
    url(r'^MostrarProveedores/$', views.MostrarProveedores, name='MostrarProveedores'),
    url(r'^MostrarBeneficioCE/$', views.MostrarBeneficioCE, name='MostrarBeneficioCE'),
    url(r'^MostrarBeneficioAlumno/$', views.MostrarBeneficioAlumno, name='MostrarBeneficioAlumno'),
    url(r'^MostrarBeneficioDocente/$', views.MostrarBeneficioDocente, name='MostrarBeneficioDocente'),
    url(r'^Reportes/$', views.reportes, name='Reportes'),


    url(r'^AgregarBeneficios/$', views.AgregarBeneficios, name='AgregarBeneficios'),
    url(r'^BeneficioCe/$', views.BeneficioCe, name='BeneficioCe'),
    url(r'^AgregarProveedor/$', views.AgregarProveedor, name='AgregarProveedor'),
    url(r'^NuevoBeneficioAlumno/$', views.BeneficioAlumno, name='BeneficioAlumno'),
    url(r'^NuevoBeneficioDocente/$', views.BeneficioDocente, name='BeneficioDocente'),


    url(r'^editarBeneficio/(?P<beneficio_id>.*)$', views.editarBeneficio, name='editarBeneficio'),
    url(r'^eliminarBeneficio/(?P<beneficio_id>.*)$', views.eliminarBeneficio, name='eliminarBeneficio'),
    url(r'^DesactivarBeneficioCe/(?P<beneficio_id>.*)$', views.DesactivarBeneficioCe, name='DesactivarBeneficioCe'),
    url(r'^DesactivarBeneficioAlumno/(?P<beneficio_id>.*)$', views.DesactivarBeneficioAlumno, name='DesactivarBeneficioAlumno'),
    url(r'^eliminarProveedor/(?P<proveedor_id>.*)$', views.eliminarProveedor, name='eliminarProveedor'),
    url(r'^editarProveedor/(?P<proveedor_id>.*)$', views.editarProveedor, name='editarProveedor'),
    )