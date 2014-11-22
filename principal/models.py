from django.db import models

# Create your models here.

class Mascota(models.Model):
	nombre = models.CharField(max_length=50)
	raza = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=400)
	edad = models.IntegerField();
	sexo = models.CharField(max_length=10)
	ubicacion = models.CharField(max_length=100)
	foto = models.ImageField(verbose_name= 'foto')

	def  __unicode__(self):
		return u'%s %s' % (self.id, self.nombre)


	

