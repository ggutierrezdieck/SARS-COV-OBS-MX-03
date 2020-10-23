from django.contrib import admin
from .models import (paciente, cuestionario, embarazo, viajes, morbilidad,
                     habitosSaludables, sintomasCovid, tratamientoCovid,
                     antecedentesEpidimiologicos, pruebas, seguridadSocial,
                     seguimiento, datosGralPaciente, medicamento)

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
admin.site.register(seguridadSocial)
admin.site.register(seguimiento)
admin.site.register(datosGralPaciente)
admin.site.register(medicamento)
