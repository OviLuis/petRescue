from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager



from django.db.models.query import QuerySet



class MiUsuarioManager(BaseUserManager):

    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('El email debe ingresarse')
        email = self.normalize_email(email)
        user = self.model(email=email, is_active=True, is_staff=is_staff, is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self,  email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    #docstring for Friki
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=55)
    direccion = models.CharField(max_length=50, null=True)
    telefono = models.CharField(max_length=15, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = MiUsuarioManager()

    #campo login
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre']

    def get_short_name(self):
        return self.nombre

    def __unicode__(self):
        return u'%s %s' % (self.id, self.nombre)


class Publicacion(models.Model):
    """docstring for Publicacion"""
    usuario = models.ForeignKey(Usuario, editable=False)

    class Meta:
        abstract = True


def content_file_name(instance, filename):
    return '/'.join(['mascotas', "o", filename])


from PIL import Image as Img
import StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile


import datetime
from django.utils import timezone


class Mascota(Publicacion):
    nombre = models.CharField(max_length=50)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    foto = models.ImageField(upload_to=content_file_name, verbose_name='Imagen')
    descripcion = models.CharField(max_length=400, verbose_name="Descripcion")
    fechaPublicacion = models.DateField(auto_now=True, editable=False)


    #class Meta:
        #abstract = True
    def __unicode__(self):
        return u'%s %s' % (self.id, self.nombre)

    def save(self, *args, **kwargs):
        if self.foto:
            size = 400, 400
            image = Img.open(StringIO.StringIO(self.foto.read()))
            image.thumbnail(size, Img.ANTIALIAS)
            output = StringIO.StringIO()
            image.save(output, format='JPEG', quality=75)
            output.seek(0)
            self.foto = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.id, 'image/jpeg', output.len, None)
        super(Mascota, self).save(*args, **kwargs)
    
    def was_published_recently(self):
        return self.fechaPublicacion >= timezone.now() - datetime.timedelta(days=1)



class Comentario(Publicacion):
    """docstring for Comentario"""
    texto = models.CharField(max_length=300)
    mascota = models.ForeignKey(Mascota)
    fechaPublicacion = models.DateTimeField(auto_now=True, editable=False)


    def __unicode__(self):
        return u'%s - %s' % (self.id, self.mascota)


class Perdidos(Mascota):
    fechaDesaparicion = models.CharField(max_length=15, help_text='AAAA/MM/DD')
    dirDesaparicion = models.CharField(max_length=50)


class Encontrados(Mascota):
    fechaEncuentro = models.CharField(max_length=15, help_text='AAAA/MM/DD')
    dirEncuentro = models.CharField(max_length=50)


class Adopciones(Mascota):
    direccion = models.CharField(max_length=50)
