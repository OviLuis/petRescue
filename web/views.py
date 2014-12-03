from principal.models import *
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from principal.forms import *
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse

from django.http import HttpResponse

from django.http import Http404

from principal.models import *

# Create your views here.


def home(request):
    return render_to_response('index.html', {'loguin_form': loguinForm()}, context_instance=RequestContext(request))


def perdidos(request):
    return render_to_response('perdidos.html', context_instance=RequestContext(request))


def reportarPerdido(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            formulario = PerdidosForm(request.POST, request.FILES)
            if formulario.is_valid():
                model_instance = formulario.save(commit=False)
                model_instance.usuario = request.user
                model_instance.save()
                return HttpResponseRedirect(reverse('web:detail', kwargs={"mascota_id": model_instance.id}))
        else:
            formulario = PerdidosForm()

        return render_to_response('perdidosform.html', {'formulario': formulario}, context_instance=RequestContext(request))
    else:
        return render_to_response('403.html', context_instance=RequestContext(request))


def encontrados(request):
    return render_to_response('encontrados.html', context_instance=RequestContext(request))


def reportarEncontrado(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            formulario = EncontradosForm(request.POST, request.FILES)
            if formulario.is_valid():
                model_instance = formulario.save(commit=False)
                model_instance.usuario = request.user
                model_instance.save()
                return HttpResponseRedirect(reverse('web:detail', kwargs={"mascota_id": model_instance.id}))
        else:
            formulario = EncontradosForm()

        return render_to_response('encontradosform.html', {'formulario': formulario}, context_instance=RequestContext(request))
    else:
        return render_to_response('403.html', context_instance=RequestContext(request))


def adopcion(request):
    return render_to_response('adopcion.html', context_instance=RequestContext(request))


def reportarAdopcion(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            formulario = AdopcionesForm(request.POST, request.FILES)
            if formulario.is_valid():
                model_instance = formulario.save(commit=False)
                model_instance.usuario = request.user
                model_instance.save()
                return HttpResponseRedirect(reverse('web:detail', kwargs={"mascota_id": model_instance.id}))
        else:
            formulario = AdopcionesForm()

        return render_to_response('adopcionesform.html', {'formulario': formulario}, context_instance=RequestContext(request))
    else:
        return render_to_response('403.html', context_instance=RequestContext(request))


def inicio(request):
    usuario = request.user
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid:
            return HttpResponseRedirect(reverse('web:inicio'))
    else:
        formulario = UsuarioForm()

    perdidos = Perdidos.objects.order_by('-fechaPublicacion')[:3]
    encontradas = Encontrados.objects.order_by('-fechaPublicacion')[:3]
    adoptados = Adopciones.objects.order_by('-fechaPublicacion')[:3]

    return render_to_response('index.html', {'formulario': formulario, 'usuario': usuario, 'perdidos': perdidos,'encontradas': encontradas,'adoptados': adoptados }, context_instance=RequestContext(request))



from django.contrib.contenttypes.models import ContentType

def detail(request, mascota_id):
    try:
        mascota = Adopciones.objects.get(pk=mascota_id)
        return render_to_response('detalleMascotaAdoptada.html', {'mascota': mascota}, context_instance=RequestContext(request))
    except Adopciones.DoesNotExist:
        try:
            mascota = Encontrados.objects.get(pk=mascota_id)
            return render_to_response('detalleMascotaEncontrada.html', {'mascota': mascota}, context_instance=RequestContext(request))
        except Encontrados.DoesNotExist:
            try:
                mascota = Perdidos.objects.get(pk=mascota_id)
                return render_to_response('detalleMascotaPerdida.html', {'mascota': mascota}, context_instance=RequestContext(request))
            except Perdidos.DoesNotExist:
                raise Http404

    return render_to_response('detalleMascota.html', {'mascota': mascota}, context_instance=RequestContext(request))


def ayuda (request):
    return render_to_response('ayuda.html', context_instance=RequestContext(request));


def miCuenta (request):
    usuario = request.user
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid:
            return HttpResponseRedirect(reverse('web:inicio'))
    else:
        formulario = UsuarioForm()
    return render_to_response('miCuenta.html',{'formulario': formulario, 'usuario': usuario, },  context_instance=RequestContext(request));


def error404(request):
    return render_to_response('404.html', context_instance=RequestContext(request))

