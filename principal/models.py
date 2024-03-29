#encoding: utf-8
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Receta(models.Model):
	"""docstring for Receta"""
	titulo = models.CharField(max_length=100, unique=True)
	ingredientes = models.TextField(help_text='Redacta los ingredientes')
	preparacion = models.TextField(verbose_name='Preparación')
	imagen = models.ImageField(upload_to='recetas', verbose_name='Imágen')
	tiempo_registro = models.DateTimeField(auto_now=True)
	usuario = models.ForeignKey(User)

	def __unicode__(self):
		return self.titulo

class Comentario(models.Model):
	"""docstring for Comentario"models.Model"""
	receta = models.ForeignKey(Receta)
	Texto = models.TextField(help_text='Tu Comentario', verbose_name='Comentario')

	def __unicode__(self):
		return self.Texto
		