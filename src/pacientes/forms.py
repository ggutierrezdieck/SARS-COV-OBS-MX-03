from django import forms
from .models import (paciente, cuestionario, embarazo, viajes, morbilidad,
                     habitosSaludables, sintomasCovid, tratamientoCovid,
                     antecedentesEpidimiologicos, pruebas)


class pacienteForm(forms.ModelForm):
    class Meta:
        model = paciente
        fields = ['id', 'fechaNacimiento', 'fechaNacimiento', 'sexo', 'escolaridad',
                  'etnicidad', 'nacionalidad', 'calle', 'colonia', 'estado',
                  'cp', 'telefono', 'ocupacion']
