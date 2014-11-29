import os


def populate():
    print "populate"
    usuario = add_usuario()
    #add_perdido(usuario)
    #add_comentario(usuario)


def add_comentario(usuario):
    comentario = Comentario(usuario=usuario, texto="Populate")


def add_usuario():
    usuario = Usuario(email="populate@populate.com", nombre="populate", direccion="populate", telefono="121212", password="populate")
    usuario.save()
    return usuario


def add_perdido(u):
    print "add perdido"
    p = Perdidos(nombre="Populate",especie="populate", raza="populate", edad="12",  sexo="populate", foto="", descripcion="populate", fechaDesaparicion="2014-11-28",dirDesaparicion="Populate", usuario=u)
    p.save()

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'petRescue.settings')
    from principal.models import *
    populate()
