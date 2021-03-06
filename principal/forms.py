# -*- coding: utf-8 -*-

from django.forms import ModelForm
from django import forms
from principal.models import *



class MascotaForm(ModelForm):
    class Meta:
            model = Mascota


class PerdidosForm(ModelForm):
    nombre = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Nombre*'}))
    especie = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Especie*', 'data-toggle':'tooltip', 'data-placement': 'right', 'title': 'tipo de mascotas ej: perro'}))
    raza = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Raza*'}))
    sexo = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Sexo*'}))
    fechaDesaparicion = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fecha Desaparicion*', 'data-toggle':'tooltip', 'data-placement': 'right', 'title': 'Formato: aaaa/mm/dd'}))
    dirDesaparicion = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Direccion*'}))
    descripcion = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Descripcion*'}))

    class Meta:
            model = Perdidos
            fields = ['nombre', 'especie', 'raza', 'sexo', 'fechaDesaparicion', 'dirDesaparicion', 'descripcion', 'foto']


class EncontradosForm(ModelForm):
    nombre = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Nombre*'}))
    especie = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Especie*' , 'data-toggle':'tooltip', 'data-placement': 'right', 'title': 'tipo de mascotas ej: perro'}))
    raza = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Raza*'}))
    sexo = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sexo*'}))
    fechaEncuentro = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fecha del encuentro*', 'data-toggle':'tooltip', 'data-placement': 'right', 'title': 'Formato: aaaa/mm/dd'}))
    dirEncuentro = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección*'}))
    descripcion = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripción*'}))

    class Meta:
            model = Encontrados
            fields = ['nombre', 'especie', 'raza', 'sexo', 'fechaEncuentro', 'dirEncuentro', 'descripcion', 'foto']


class AdopcionesForm(ModelForm):
    nombre = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Nombre*'}))
    especie = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Especie*', 'data-toggle':'tooltip', 'data-placement': 'right', 'title': 'tipo de mascotas ej: perro'}))
    raza = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Raza*'}))
    sexo = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Sexo*'}))
    direccion = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Dirección*'}))
    descripcion = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Descripción*'}))

    class Meta:
            model = Adopciones
            fields = ['nombre', 'especie', 'raza', 'sexo', 'direccion', 'descripcion', 'foto']


class UsuarioForm(ModelForm):
    nombre = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Nombre*'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Correo Electronico*', 'data-toggle':'tooltip', 'data-placement': 'top', 'title': 'example@correo.com'}))
    direccion = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Dirección*'}))
    telefono = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Numero Telefonico*'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Contraseña*', 'for': 'id_password'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Confirmar Contraseña*', 'for': 'id_password2'}))

    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'direccion', 'telefono', 'password']

    def save(self, commit=True):
        user = super(UsuarioForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
