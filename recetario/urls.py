from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^recetas','principal.views.lista_recetas'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root':settings.MEDIA_ROOT,}),
    url(r'^sobre/$','principal.views.sobre'),
    url(r'^$','principal.views.inicio'),
    url(r'^usuarios/$','principal.views.usuarios'),
    url(r'^receta/(?P<id_receta>\d+)$','principal.views.detalle_receta'),
    url(r'^contacto/$', 'principal.views.contacto'),
    url(r'^receta/nueva/$', 'principal.views.nueva_receta'),
    url(r'^comenta/$', 'principal.views.nuevo_comentario'),
    url(r'^usuario/nuevo/$', 'principal.views.nuevo_usuario'),
    url(r'^ingresar/$', 'principal.views.ingresar'),
    url(r'^privado/$', 'principal.views.privado'),
    url(r'^cerrar/$', 'principal.views.cerrar'),
)