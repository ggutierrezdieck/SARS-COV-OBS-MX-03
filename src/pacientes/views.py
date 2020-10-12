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
    # Calling the right methdod whenposting from within the ajax content
    if request.method == 'POST':
        if 'fechaNacimiento' in request.POST.keys():
            nuevo_view(request)
        elif 'folio' in request.POST.keys():
            questionnaire_view(request, request.POST['paciente'])
    return render(request, 'index.html', context)


def questionnaire_view(request, id):
    context = {'id': id}

    # Getting inctances for the requested id
    try:
        cue = cuestionario.objects.get(paciente=id)
    except ObjectDoesNotExist:
        cue = None
    try:
        emb = embarazo.objects.get(paciente=id)
    except ObjectDoesNotExist:
        emb = None
    try:
        via = viajes.objects.get(paciente=id)
    except ObjectDoesNotExist:
        via = None
    try:
        mor = morbilidad.objects.get(paciente=id)
    except ObjectDoesNotExist:
        mor = None
    try:
        hab = habitosSaludables.objects.get(paciente=id)
    except ObjectDoesNotExist:
        hab = None
    try:
        sin = sintomasCovid.objects.get(paciente=id)
    except ObjectDoesNotExist:
        sin = None
    try:
        tra = tratamientoCovid.objects.get(paciente=id)
    except ObjectDoesNotExist:
        tra = None
    try:
        ant = antecedentesEpidimiologicos.objects.get(paciente=id)
    except ObjectDoesNotExist:
        ant = None
    try:
        pru = pruebas.objects.get(paciente=id)
    except ObjectDoesNotExist:
        pru = None

    # Createing questionairs with intances created above
    fcuestionario = cuestionarioForm(instance=cue)
    fembarazo = embarazoForm(instance=emb)
    fviajes = viajesForm(instance=via)
    fmorbilidad = morbilidadForm(instance=mor)
    fhabitos = habitosSaludablesForm(instance=hab)
    fsintomas = sintomasCovidForm(instance=sin)
    ftrataminto = tratamientoCovidForm(instance=tra)
    fanteceddentes = antecedentesEpidimiologicosForm(instance=ant)
    fpruebas = pruebasForm(instance=pru)

    if request.method == 'POST':
        fcuestionario = cuestionarioForm(request.POST, instance=cue)
        fembarazo = embarazoForm(request.POST, instance=emb)
        fviajes = viajesForm(request.POST, instance=via)
        fmorbilidad = morbilidadForm(request.POST, instance=mor)
        fhabitos = habitosSaludablesForm(request.POST, instance=hab)
        fsintomas = sintomasCovidForm(request.POST, instance=sin)
        ftrataminto = tratamientoCovidForm(request.POST, instance=tra)
        fanteceddentes = antecedentesEpidimiologicosForm(request.POST, instance=ant)
        fpruebas = pruebasForm(request.POST, instance=pru)

        forms = [fcuestionario, fembarazo, fviajes, fmorbilidad, fhabitos,
                 fsintomas, ftrataminto, fanteceddentes, fpruebas]
        valid_forms = 0
        print(forms)
        for form in forms:
            print(form)
            print(form.is_valid())
            print(form.is_bound)
            if form.is_valid():
                add_id = form.save(commit=False)
                add_id.paciente = get_object_or_404(paciente, pk=id)
                add_id.save()
                valid_forms += 1
                if valid_forms == len(forms):
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
    # print(request.method)
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
