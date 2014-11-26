from django.contrib import admin
from  principal.models import *
# Register your models here.


#admin.site.register(Mascota) #No se registra porque es abstracta
admin.site.register(Comentario)
admin.site.register(Perdidos)
admin.site.register(Encontrados)
admin.site.register(Adopciones)
admin.site.register(Usuario)
