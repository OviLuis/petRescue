from principal.models import *
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from principal.forms import *
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse

from principal.models import *

# Create your views here.


def home(request):
    return render_to_response('inicio.html', context_instance=RequestContext(request))


def perdidos(request):
    return render_to_response('perdidos.html', context_instance=RequestContext(request))


def reportarPerdido(request):
    if request.method == 'POST':
        formulario = PerdidosForm(request.POST, request.FILES)
        if formulario.is_valid():
            return HttpResponseRedirect(reverse('web:perdidos'))
    else:
        formulario = PerdidosForm()

    return render_to_response('perdidosform.html', {'formulario': formulario}, context_instance=RequestContext(request))


def encontrados(request):
    return render_to_response('encontrados.html', context_instance=RequestContext(request))


def reportarEncontrado(request):
    if request.method == 'POST':
        formulario = EncontradosForm(request.POST, request.FILES)
        if formulario.is_valid():
            return HttpResponseRedirect(reverse('web:reportarEncontrado'))
    else:
        formulario = EncontradosForm()

    return render_to_response('encontradosform.html', {'formulario': formulario}, context_instance=RequestContext(request))


def adopcion(request):
    return render_to_response('adopcion.html', context_instance=RequestContext(request))


def reportarAdopcion(request):
    if request.method == 'POST':
        formulario = AdopcionesForm(request.POST, request.FILES)
        if formulario.is_valid():
            return HttpResponseRedirect('/adopciones')
    else:
        formulario = AdopcionesForm()

    return render_to_response('adopcionesform.html', {'formulario': formulario}, context_instance=RequestContext(request))


def inicio(request):
    usuario = request.user
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid:
            return HttpResponseRedirect(reverse('web:home'))
    else:
        formulario = UsuarioForm()
    return render_to_response('home.html', {'formulario': formulario, 'usuario': usuario}, context_instance=RequestContext(request))
