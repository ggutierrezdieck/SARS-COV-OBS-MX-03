from django.shortcuts import render
from django.shortcuts import get_object_or_404
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

    fcuestionario = cuestionarioForm(cue)
    fembarazo = embarazoForm(emb)
    fviajes = viajesForm(via)
    fmorbilidad = morbilidadForm(mor)
    fhabitos = habitosSaludablesForm(hab)
    fsintomas = sintomasCovidForm(sin)
    ftrataminto = tratamientoCovidForm(tra)
    fanteceddentes = antecedentesEpidimiologicosForm(ant)
    fpruebas = pruebasForm(pru)
    print(request.method)
    if request.method == 'POST':
        fcuestionario = cuestionarioForm(request.POST)
        if fcuestionario.is_valid():
            print(id)
            add_id = fcuestionario.save(commit=False)
            add_id.paciente = get_object_or_404(paciente, pk=id)
            add_id.save()
            return render(request, 'index.html', context)
        else:
            print('One form is not valid')
    else:
        context['fcuestionario'] = fcuestionario
        context['fembarazo'] = fembarazo
        context['fviajes'] = fviajes
        context['fmorbilidad'] = fmorbilidad
        context['fhabitos'] = fhabitos
        context['fsintomas'] = fsintomas
        context['ftrataminto'] = ftrataminto
        context['fanteceddentes'] = fanteceddentes
        context['fpruebas'] = fpruebas

    return render(request, 'questionnaire.html', context)


def nuevo_view(request):
    queryset = len(paciente.objects.all()) + 1
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
