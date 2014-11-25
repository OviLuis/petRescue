from django.forms import ModelForm
from django import forms
from principal.models import Mascota


class MascotaForm(ModelForm):
	class Meta:
			model = Mascota
