from django.db import models

# Create your models here.

class Mascota(models.Model):
	nombre = models.CharField(max_length=50)
	raza = models.CharField(max_length=50)	
	edad = models.IntegerField()
	especie = models.CharField(max_length=50)
	sexo = models.CharField(max_length=10)
	foto = models.ImageField(verbose_name= 'foto')
	descripcion = models.CharField(max_length=400)
	

	def  __unicode__(self):
		return u'%s %s' % (self.id, self.nombre)


class Perdidos(Mascota):
	fechaDesaparicion = models.DateTimeField(auto_now=True)
	dirDesaparicion = models.CharField(max_length=50)

	def __unicode__(self):
		return u'%s' % (self.id)


class Encontrados(Mascota):
	fechaEncuentro = models.DateTimeField()
	dirEncuentro = models.CharField(max_length=50)

	def __unicode__(self):
		return u'%s' % (self.id)


class Adopciones(Mascota):
	direccion = models.CharField(max_length=59)

	def __unicode__(self):
		return u'%s' % (self.id)



		


	

