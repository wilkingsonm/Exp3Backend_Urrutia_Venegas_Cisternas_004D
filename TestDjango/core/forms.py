from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import widget
from . models import Categoria, Vehiculo

class VehiculoForm(forms.ModelForm):

    class Meta:
        model= Vehiculo
        Fields = ['patente', 'marca', 'modelo', 'categoria']
        labels = {
            'patente': 'Patente de vehiculo',
            'marca': 'Marca de vehiculo',
            'Modelo': 'Modelo de vehiculo',
            'Categoria': 'Categoria de vehiculo',
        }

        widgets={
            'patente': forms.TextInput{
                attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese patente',
                'id': 'patente'
                }
            }
            'marca': forms.TextInput{
                attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese marca',
                'id': 'marca'
                }
            }
            'modelo': forms.TextInput{
                attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese modelo',
                'id': 'modelo'
                }
            }
            'categoria': forms.Select{
                attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese categoria',
                'id': 'categoria'
                }
            }
        }


        
