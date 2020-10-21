from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import (pacienteForm, cuestionarioForm, embarazoForm, viajesForm,
                    morbilidadForm, habitosSaludablesForm, sintomasCovidForm,
                    tratamientoCovidForm, antecedentesEpidimiologicosForm,
                    pruebasForm, seguridadSocialForm, datosGralPacienteForm,
                    medicamentoForm, seguimientoForm)
from .models import (paciente, cuestionario, embarazo, viajes, morbilidad,
                     habitosSaludables, sintomasCovid, tratamientoCovid,
                     antecedentesEpidimiologicos, pruebas, seguridadSocial,
                     datosGralPaciente, medicamento, seguimiento)

# Create your views here.


@login_required
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


@login_required
def questionnaire_view(request, id):
    context = {'id': id}

    # Getting inctances for the requested id
    try:
        dgp = datosGralPaciente.objects.get(paciente=id)
    except ObjectDoesNotExist:
        dgp = None
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
        med = medicamento.objects.get(paciente=id)
    except ObjectDoesNotExist:
        med = None
    try:
        ant = antecedentesEpidimiologicos.objects.get(paciente=id)
    except ObjectDoesNotExist:
        ant = None
    try:
        pru = pruebas.objects.get(paciente=id)
    except ObjectDoesNotExist:
        pru = None
    try:
        sso = seguridadSocial.objects.get(paciente=id)
    except ObjectDoesNotExist:
        sso = None
    try:
        seg = seguimiento.objects.get(paciente=id)
    except ObjectDoesNotExist:
        seg = None

    # Createing questionairs with intances created above
    fgeneales = datosGralPacienteForm(instance=dgp)
    fcuestionario = cuestionarioForm(instance=cue)
    fembarazo = embarazoForm(instance=emb)
    fviajes = viajesForm(instance=via)
    fmorbilidad = morbilidadForm(instance=mor)
    fhabitos = habitosSaludablesForm(instance=hab)
    fsintomas = sintomasCovidForm(instance=sin)
    ftrataminto = tratamientoCovidForm(instance=tra)
    fmedicamento = medicamentoForm(instance=med)
    fanteceddentes = antecedentesEpidimiologicosForm(instance=ant)
    fpruebas = pruebasForm(instance=pru)
    fseguridad = seguridadSocialForm(instance=sso)
    fseguimiento = seguimientoForm(instance=seg)

    if request.method == 'POST':
        fgeneales = datosGralPacienteForm(request.POST, instance=dgp)
        fcuestionario = cuestionarioForm(request.POST, instance=cue)
        fembarazo = embarazoForm(request.POST, instance=emb)
        fviajes = viajesForm(request.POST, instance=via)
        fmorbilidad = morbilidadForm(request.POST, instance=mor)
        fhabitos = habitosSaludablesForm(request.POST, instance=hab)
        fsintomas = sintomasCovidForm(request.POST, instance=sin)
        ftrataminto = tratamientoCovidForm(request.POST, instance=tra)
        fmedicamento = medicamentoForm(request.POST, instance=med)
        fanteceddentes = antecedentesEpidimiologicosForm(request.POST, instance=ant)
        fpruebas = pruebasForm(request.POST, instance=pru)
        fseguridad = seguridadSocialForm(request.POST, instance=sso)
        fseguimiento = seguimientoForm(request.POST, instance=seg)

        forms = [fgeneales, fcuestionario, fembarazo, fviajes, fmorbilidad,
                 fhabitos, fsintomas, ftrataminto, fmedicamento, fanteceddentes,
                 fpruebas, fseguridad,fseguimiento]
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
        context['fgeneales'] = fgeneales
        context['fcuestionario'] = fcuestionario
        context['fembarazo'] = fembarazo
        context['fviajes'] = fviajes
        context['fmorbilidad'] = fmorbilidad
        context['fhabitos'] = fhabitos
        context['fsintomas'] = fsintomas
        context['ftrataminto'] = ftrataminto
        context['fmedicamento'] = fmedicamento
        context['fanteceddentes'] = fanteceddentes
        context['fpruebas'] = fpruebas
        context['fseguridad'] = fseguridad
        context['fseguimiento'] = fseguimiento

    return render(request, 'questionnaire.html', context)


@login_required
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
