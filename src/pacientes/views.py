from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .forms import (pacienteForm, cuestionarioForm, embarazoForm, viajesForm,
                    morbilidadForm, habitosSaludablesForm, sintomasCovidForm,
                    tratamientoCovidForm, antecedentesEpidimiologicosForm,
                    pruebasForm)
from .models import (paciente, cuestionario, embarazo, viajes, morbilidad,
                     habitosSaludables, sintomasCovid, tratamientoCovid,
                     antecedentesEpidimiologicos, pruebas)

# Create your views here.


def index_view(request):
    queryset = paciente.objects.all()
    context = {
        'pacientes': queryset
    }
    return render(request, 'index.html', context)


def questionnaire_view(request, id):
    context = {'id': id}
    # pac = paciente.objects.get(pk=id)
    try:
        cue = cuestionario.objects.get(paciente=id)
        emb = embarazo.objects.get(paciente=id)
        via = viajes.objects.get(paciente=id)
        mor = morbilidad.objects.get(paciente=id)
        hab = habitosSaludables.objects.get(paciente=id)
        sin = sintomasCovid.objects.get(paciente=id)
        tra = tratamientoCovid.objects.get(paciente=id)
        ant = antecedentesEpidimiologicos.objects.get(paciente=id)
        pru = pruebas.objects.get(paciente=id)
    except ObjectDoesNotExist:
        cue = None
        emb = None
        via = None
        mor = None
        hab = None
        sin = None
        tra = None
        ant = None
        pru = None

    # if request.method == 'POST':
    #     form = pacienteForm(request.POST or None)
    #     if form.is_valid():
    #         form.save()
    #         # message.success(request, ('textmessate'))
    #         return render(request, 'index.html', context)
    # else:

    context['fcuestionario'] = cuestionarioForm(cue)
    context['fembarazo'] = embarazoForm(emb)
    context['fviajes'] = viajesForm(via)
    context['fmorbilidad'] = morbilidadForm(mor)
    context['fhabitos'] = habitosSaludablesForm(hab)
    context['fsintomas'] = sintomasCovidForm(sin)
    context['ftrataminto'] = tratamientoCovidForm(tra)
    context['fanteceddentes'] = antecedentesEpidimiologicosForm(ant)
    context['fpruebas'] = pruebasForm(pru)

    return render(request, 'questionnaire.html', context)


def nuevo_view(request):
    queryset = len(paciente.objects.all())
    context = {
        'last_id': queryset
    }

    if request.method == 'POST':
        form = pacienteForm(request.POST or None)
        if form.is_valid():
            form.save()
            # message.success(request, ('textmessate'))
            return render(request, 'newPatient.html', context)
    else:
        form = pacienteForm()
        context['form'] = form
        return render(request, 'newPatient.html', context)

