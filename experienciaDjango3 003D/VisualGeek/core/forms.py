from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Categoria, Emisor


class EmisorForm(forms.ModelForm):

    class Meta: 
        model= Emisor
        fields = ['nombre', 'apellido', 'edad', 'email', 'resumen','categoria']
        labels ={
            'nombre': '', 
            'apellido': '', 
            'edad': '', 
            'email': '',
            'categoria': '',
            'resumen': '',
        }
        widgets={
            'email': forms.TextInput(
                attrs={
                    'class': 'barra', 
                    'placeholder': 'Ingrese email', 
                    'id': 'email'
                }
            ), 
            'edad': forms.TextInput(
                attrs={
                    'class': 'barra', 
                    'placeholder': 'Ingrese edad', 
                    'id': 'edad'
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'barra', 
                    'placeholder': 'Ingrese nombre', 
                    'id': 'nombre'
                }
            ), 
            'apellido': forms.TextInput(
                attrs={
                    'class': 'barra', 
                    'placeholder': 'Ingrese apellido', 
                    'id': 'apellido'
                }
            ), 
            'categoria': forms.Select(
                attrs={
                    'class': 'barra',
                    'id': 'categoria',
                }
            ),
            'resumen': forms.TextInput(
                attrs={
                    'class': 'barra', 
                    'placeholder': 'Ingrese resumen', 
                    'id': 'resumen'
                }
            ), 

        }

 
    
     
