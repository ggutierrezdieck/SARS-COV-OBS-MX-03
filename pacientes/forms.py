from django import forms
from .models import (paciente, cuestionario, embarazo, viajes, morbilidad,
                     habitosSaludables, sintomasCovid, tratamientoCovid,
                     antecedentesEpidimiologicos, pruebas)


class pacienteForm(forms.ModelForm):
    class Meta:
        model = paciente
        fields = ['id', 'fechaNacimiento', 'sexo',
                  'escolaridad', 'etnicidad', 'nacionalidad', 'calle', 
                  'colonia', 'estado', 'cp', 'telefono', 'ocupacion']
        widgets = {
                    'fechaNacimiento': forms.DateInput(
                                                        format=('%d-%m-%Y'),
                                                        attrs={
                                                                'type': 'date',
                                                                'class': 'date_picker',
                                                                }),
                  }


class cuestionarioForm(forms.ModelForm):
    class Meta:
        model = cuestionario
        fields = '__all__'
        exclude = ['paciente']
        widgets = {
                    'fechaCuestioario': forms.DateInput(attrs={
                                                                'type': 'date',
                                                                }),
                    }


class embarazoForm(forms.ModelForm):
    class Meta:
        model = embarazo
        fields = '__all__'
        exclude = ['paciente']


class viajesForm(forms.ModelForm):
    class Meta:
        model = viajes
        fields = '__all__'
        exclude = ['paciente']


class morbilidadForm(forms.ModelForm):
    class Meta:
        model = morbilidad
        fields = '__all__'
        exclude = ['paciente']


class habitosSaludablesForm(forms.ModelForm):
    class Meta:
        model = habitosSaludables
        fields = '__all__'
        exclude = ['paciente']


class sintomasCovidForm(forms.ModelForm):
    class Meta:
        model = sintomasCovid
        fields = '__all__'
        exclude = ['paciente']


class tratamientoCovidForm(forms.ModelForm):
    class Meta:
        model = tratamientoCovid
        fields = '__all__'
        exclude = ['paciente']


class antecedentesEpidimiologicosForm(forms.ModelForm):
    class Meta:
        model = antecedentesEpidimiologicos
        fields = '__all__'
        exclude = ['paciente']


class pruebasForm(forms.ModelForm):
    class Meta:
        model = pruebas
        fields = '__all__'
        exclude = ['paciente']
