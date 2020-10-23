from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.http import QueryDict
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
        med = medicamento.objects.all().filter(paciente=id)
        if len(med) == 0:
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
    # fmedicamento = medicamentoForm(instance=med)
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
        # fmedicamento = medicamentoForm(request.POST, instance=med)
        fanteceddentes = antecedentesEpidimiologicosForm(request.POST, instance=ant)
        fpruebas = pruebasForm(request.POST, instance=pru)
        fseguridad = seguridadSocialForm(request.POST, instance=sso)
        fseguimiento = seguimientoForm(request.POST, instance=seg)

        valid_forms = 0

        # Handling fmedicamento specially, this special case allows for multiple submissions in one go
        # Saving post as dictionary
        postDict = request.POST.dict()
        # making list from field names from model
        medicamentoFields = [f.name for f in medicamento._meta.get_fields()]
        #  Crating query dick
        medicamentoPosts = [QueryDict('', mutable=True)]

        for key in postDict.keys():
            if key in medicamentoFields:
                for i in range(len(request.POST.getlist(key))):
                    try:
                        medicamentoPosts[i].appendlist(key, request.POST.getlist(key)[i])
                    except IndexError:
                        medicamentoPosts.append(QueryDict('', mutable=True))
                        medicamentoPosts[i].appendlist('paciente', str(id))
                        medicamentoPosts[i].appendlist(key, request.POST.getlist(key)[i])

        for i in range(len(medicamentoPosts)):
            try:
                med = medicamento.objects.get(nombreMedicamento=medicamentoPosts[i]['nombreMedicamento'])
            except ObjectDoesNotExist:
                med = None

            fmedicamento = medicamentoForm(medicamentoPosts[i], instance=med)
            if fmedicamento.is_valid():
                add_id = fmedicamento.save(commit=False)
                add_id.paciente = get_object_or_404(paciente, pk=id)
                add_id.save()

        valid_forms += 1

        # Handling the rest of the forms
        forms = [fgeneales, fcuestionario, fembarazo, fviajes, fmorbilidad,
                 fhabitos, fsintomas, ftrataminto, fanteceddentes,
                 fpruebas, fseguridad, fseguimiento]

        for form in forms:
            if form.is_valid():
                add_id = form.save(commit=False)
                add_id.paciente = get_object_or_404(paciente, pk=id)
                add_id.save()
                valid_forms += 1
                # Checking all forms where valid, including fmedicamento
                if valid_forms == len(forms) + 1:
                    return render(request, 'index.html', context)
            else:
                print('One form is not valid')

    else:
        # Handling medicamento form independently, due to to the multipel items
        fmedicamento = None
        context['fmedicamento'] = {}
        i = 0
        try:
            for m in med:
                fmedicamento = medicamentoForm(instance=m)
                context['fmedicamento']['a' + str(i)] = fmedicamento
                i += 1
        except TypeError:
            fmedicamento = medicamentoForm(instance=med)
            context['fmedicamento'] = fmedicamento

        context['fgeneales'] = fgeneales
        context['fcuestionario'] = fcuestionario
        context['fembarazo'] = fembarazo
        context['fviajes'] = fviajes
        context['fmorbilidad'] = fmorbilidad
        context['fhabitos'] = fhabitos
        context['fsintomas'] = fsintomas
        context['ftrataminto'] = ftrataminto
        # context['fmedicamento'] = fmedicamento
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
