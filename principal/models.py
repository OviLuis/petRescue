from django.db import models


from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class MiUsuarioManager(BaseUserManager):

    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('El email debe ingresarse')
        email = self.normalize_email(email)
        user = self.model( email=email, is_active=True, is_staff=is_staff, is_superuser=is_superuser,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user( email, password,  False, False, **extra_fields)

    def create_superuser(self,  email, password, **extra_fields):
        return self._create_user( email, password,  True, True, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    #docstring for Friki
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=55)
    direccion = models.CharField(max_length=50, null=True)
    telefono = models.IntegerField(max_length=15, null=True)



    is_active = models.BooleanField (default=True)
    is_staff = models.BooleanField (default=False)

    objects = MiUsuarioManager()

    USERNAME_FIELD = 'email'    #campo login
    REQUIRED_FIELDS = ['nombre']

    def get_short_name(self):
        return self.nombre


class Publicacion(models.Model):
    """docstring for Publicacion"""
    usuario = models.ForeignKey(Usuario)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Comentario(Publicacion)
    """docstring for Comentario"""
    texto = models.CharField(max_length=300)


class Mascota(Publicacion):
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    edad = models.IntegerField()
    especie = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    foto = models.ImageField(upload_to='mascotas',verbose_name='Imagen')
    descripcion = models.CharField(max_length=400)

    class Meta:
        abstract = True

    def  __unicode__(self):
        return u'%s %s' % (self.id, self.nombre)



class Perdidos(Mascota):
    fechaDesaparicion = models.DateTimeField()
    dirDesaparicion = models.CharField(max_length=50)


class Encontrados(Mascota):
    fechaEncuentro = models.DateTimeField()
    dirEncuentro = models.CharField(max_length=50)


class Adopciones(Mascota):
    direccion = models.CharField(max_length=59)