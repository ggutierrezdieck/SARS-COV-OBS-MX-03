from django import forms
from .models import (paciente, cuestionario, embarazo, viajes, morbilidad,
                     habitosSaludables, sintomasCovid, tratamientoCovid,
                     antecedentesEpidimiologicos, pruebas, seguridadSocial,
                     seguimiento, datosGralPaciente, medicamento)


class pacienteForm(forms.ModelForm):
    class Meta:
        model = paciente
        fields = '__all__'
        widgets = {
                    'fechaNacimiento': forms.DateInput(
                                                        format=('%d-%m-%Y'),
                                                        attrs={
                                                                'type': 'date',
                                                                'class': 'date_picker',
                                                                }),
                    'fechaIngresoDeExtrangero': forms.DateInput(
                                                        format=('%d-%m-%Y'),
                                                        attrs={'type': 'date',}),
                  }  



class datosGralPacienteForm(forms.ModelForm):
    class Meta:
        model = datosGralPaciente
        fields = '__all__'
        exclude = ['paciente']
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
                    'fechaCuestionario': forms.DateInput(attrs={
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
        widgets = {
                    'fechaRegreso': forms.DateInput(attrs={
                                                                'type': 'date',
                                                                }),
                    }


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
        widgets = {
                    'fechaSintomas': forms.DateInput(attrs={
                                                                'type': 'date',
                                                                }),
                    }


class tratamientoCovidForm(forms.ModelForm):
    class Meta:
        model = tratamientoCovid
        fields = '__all__'
        exclude = ['paciente']


class medicamentoForm(forms.ModelForm):
    class Meta:
        model = medicamento
        fields = '__all__'
        exclude = ['paciente']
        widgets = {
                    'fechaInicio': forms.DateInput(attrs={
                                                                'type': 'date',
                                                                }),
                    'fechaTermino': forms.DateInput(attrs={
                                                                'type': 'date',
                                                                }),
                    }


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
        widgets = {
                    'fechaInicio': forms.DateInput(attrs={
                                                                'type': 'date',
                                                                }),
                    }


class seguridadSocialForm(forms.ModelForm):
    class Meta:
        model = seguridadSocial
        fields = '__all__'
        exclude = ['paciente']


class seguimientoForm(forms.ModelForm):
    class Meta:
        model = seguimiento
        fields = '__all__'
        exclude = ['paciente']
        widgets = {
                    'fechaDefuncion': forms.DateInput(attrs={
                                                                'type': 'date',
                                                                }),
                    'fechaIngresoHospital': forms.DateInput(attrs={
                                                                'type': 'date',
                                                                }),
                    'fechaEgresoHospital': forms.DateInput(attrs={
                                                                'type': 'date',
                                                                }),
                    }
