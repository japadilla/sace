from django.conf.urls import patterns, url
from beneficios import views

urlpatterns = patterns('',
    url(r'^Beneficios/$', views.IndexBeneficios, name='IndexBeneficios'),
    url(r'^MostrarBeneficios/$', views.MostrarBeneficios, name='MostrarBeneficios'),
    url(r'^MostrarProveedores/$', views.MostrarProveedores, name='MostrarProveedores'),
    url(r'^AgregarBeneficios/$', views.AgregarBeneficios, name='AgregarBeneficios'),
    url(r'^BeneficioCe/$', views.BeneficioCe, name='BeneficioCe'),
    url(r'^AgregarProveedor/$', views.AgregarProveedor, name='AgregarProveedor'),
    url(r'^editarBeneficio/(?P<beneficio_id>.*)$', views.editarBeneficio, name='editarBeneficio'),
    url(r'^eliminarBeneficio/(?P<beneficio_id>.*)$', views.eliminarBeneficio, name='eliminarBeneficio'),
    url(r'^eliminarProveedor/(?P<proveedor_id>.*)$', views.eliminarProveedor, name='eliminarProveedor'),
    url(r'^editarProveedor/(?P<proveedor_id>.*)$', views.editarProveedor, name='editarProveedor'),
    )