from django.shortcuts import render
from .forms import pacienteForm
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


def questionnaire_view(request):
    queryset = paciente.objects.all()
    context = {
        'pacientes': queryset
    }

    if request.method == 'POST':
        form = pacienteForm(request.POST or None)
        if form.is_valid():
            form.save()
            # message.success(request, ('textmessate'))
            return render(request, 'index.html', context)
    else:
        form = pacienteForm()
        context['form'] = form
        return render(request, 'questionnaire.html', context)
