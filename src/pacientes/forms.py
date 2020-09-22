from django import forms
from .models import (paciente, cuestionario, embarazo, viajes, morbilidad,
                     habitosSaludables, sintomasCovid, tratamientoCovid,
                     antecedentesEpidimiologicos, pruebas)


class pacienteForm(forms.ModelForm):
    class Meta:
        model = paciente
        fields = ['id', 'fechaNacimiento', 'fechaNacimiento', 'sexo',
                  'escolaridad', 'etnicidad', 'nacionalidad', 'calle', 
                  'colonia', 'estado', 'cp', 'telefono', 'ocupacion']


class cuestionarioForm(forms.ModelForm):
    class Meta:
        model = cuestionario
        fields = '__all__'


class embarazoForm(forms.ModelForm):
    class Meta:
        model = embarazo
        fields = '__all__'


class viajesForm(forms.ModelForm):
    class Meta:
        model = viajes
        fields = '__all__'


class morbilidadForm(forms.ModelForm):
    class Meta:
        model = morbilidad
        fields = '__all__'


class habitosSaludablesForm(forms.ModelForm):
    class Meta:
        model = habitosSaludables
        fields = '__all__'


class sintomasCovidForm(forms.ModelForm):
    class Meta:
        model = sintomasCovid
        fields = '__all__'


class tratamientoCovidForm(forms.ModelForm):
    class Meta:
        model = tratamientoCovid
        fields = '__all__'


class antecedentesEpidimiologicosForm(forms.ModelForm):
    class Meta:
        model = antecedentesEpidimiologicos
        fields = '__all__'


class pruebasForm(forms.ModelForm):
    class Meta:
        model = pruebas
        fields = '__all__'
