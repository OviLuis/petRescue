# -*- coding: utf-8 -*-

from django.forms import ModelForm
from django import forms
from principal.models import *


class MascotaForm(ModelForm):
    class Meta:
            model = Mascota


class PerdidosForm(ModelForm):
    nombre = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Nombre'}))
    edad = forms.IntegerField(label='', widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Edad'}))
    especie = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Especie'}))
    raza = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Raza'}))
    sexo = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Genero'}))
    fechaDesaparicion = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Fecha Desaparicion'}))
    dirDesaparicion = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Direccion'}))
    descripcion = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Descripcion'}))

    class Meta:
            model = Perdidos
            fields = ['nombre', 'edad', 'especie', 'raza', 'sexo', 'fechaDesaparicion', 'dirDesaparicion', 'descripcion', 'foto']


class EncontradosForm(ModelForm):
    nombre = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Nombre'}))
    edad = forms.IntegerField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Edad'}))
    especie = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Especie'}))
    raza = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Raza'}))
    sexo = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Genero'}))
    fechaEncuentro = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fecha Desaparicion'}))
    dirEncuentro = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Direccion'}))
    descripcion = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripcion'}))

    class Meta:
            model = Encontrados
            fields = ['nombre', 'edad', 'especie', 'raza', 'sexo', 'fechaEncuentro', 'dirEncuentro', 'descripcion', 'foto']


class AdopcionesForm(ModelForm):
    nombre = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Nombre'}))
    edad = forms.IntegerField(label='', widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Edad'}))
    especie = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Especie'}))
    raza = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Raza'}))
    sexo = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Genero'}))
    direccion = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Direccion'}))
    descripcion = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Descripcion'}))

    class Meta:
            model = Adopciones
            fields = ['nombre', 'edad', 'especie', 'raza', 'sexo', 'direccion', 'descripcion', 'foto']


class UsuarioForm(ModelForm):
    nombre = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Nombre'}))
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Correo Electronico'}))
    direccion = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Direccion'}))
    telefono = forms.IntegerField(label='', widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Numero Telefonico'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Contraseña'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Confirmar Contraseña'}))

    class Meta:
        model = Usuario
        fields = []


class loguinForm(forms.Form):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Correo Electronico'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Contraseña'}))
