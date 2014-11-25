from django.forms import ModelForm
from django import forms
from principal.models import *


class MascotaForm(ModelForm):
	class Meta:
			model = Mascota


class PerdidosForm(ModelForm):
	class Meta:
			model = Perdidos


class EncontradosForm(ModelForm):
	class Meta:
			model = Encontrados



class AdopcionesForm(ModelForm):
	class Meta:
			model = Adopciones
			
		
			
		
	
		
