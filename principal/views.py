from principal.models import *
from django.template.context import RequestContext
from django.shortcuts import render_to_response

# Create your views here.

def inicio(request):
	return render_to_response('inicio.html', context_instance = RequestContext(request))

def perdidos(request):
	return render_to_response ('perdidos.html', context_instance = RequestContext(request) )

def encontrados(request):
	return render_to_response ('encontrados.html', context_instance = RequestContext(request))

def adopcion(request):
	return render_to_response ('adopcion.html', context_instance = RequestContext(request));
