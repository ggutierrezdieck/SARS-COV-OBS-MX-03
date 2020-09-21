from django.contrib import admin
from .models import (paciente, cuestionario, embarazo, viajes, morbilidad,
                     habitosSaludables, sintomasCovid, tratamientoCovid,
                     antecedentesEpidimiologicos, pruebas)

# Register your models here.
admin.site.register(paciente)
admin.site.register(cuestionario)
admin.site.register(embarazo)
admin.site.register(viajes)
admin.site.register(morbilidad)
admin.site.register(habitosSaludables)
admin.site.register(sintomasCovid)
admin.site.register(tratamientoCovid)
admin.site.register(antecedentesEpidimiologicos)
admin.site.register(pruebas)
