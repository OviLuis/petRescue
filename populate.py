import os


def populate():
    print "populate"
    usuario = add_usuario()
    add_perdido(usuario)
    #add_comentario(usuario)


def add_comentario(usuario):
    comentario = Comentario(usuario=usuario, texto="Populate")


def add_usuario():
    usuario = Usuario.objects.create_user(email="populate@populate.com", nombre="populate", direccion="populate", telefono="121212", password="populate")
    return usuario


def add_perdido(usuario):
    print "add perdido"
    perdido = Perdidos(nombre="Populate",raza="populate", edad="12", especie="populate", sexo="populate", foto="C://populate.jpg", descripcion="populate", fechaDesaparicion="2014-11-28T02:31:49.658Z",dirDesaparicion="Populate", usuario=usuario)
    #perdido.save()

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'petRescue.settings')
    from principal.models import Usuario, Comentario, Perdidos
    populate()
