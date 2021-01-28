from django.db import models
from django_countries.fields import CountryField
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

SiNo = (
    ('1', 'Si'),
    ('0', 'No')
)


class paciente(models.Model):

    def __str__(self):
        return 'Paciente ' + str(self.id)

    GENEROS = (
        ('H', 'Hombre'),
        ('M', 'Mujer')
    )
    fechaNacimiento = models.DateField(verbose_name='Fecha de Nacimiento')
    sexo = models.CharField(max_length=120, choices=GENEROS)
    nacionalidad = CountryField()
    fechaIngresoDeExtrangero = models.DateField(blank=True, null=True, verbose_name='Fecha de ingreso a México')


class datosGralPaciente(models.Model):

    def __str__(self):
        return 'Paciente ' + str(self.id)

    ESCOLARIDADES = (
        ('N', 'Ninguna'),
        ('P', 'Primaria'),
        ('S', 'Secundaria'),
        ('B', 'Bachillerato'),
        ('L', 'Licenciatura'),
        ('M', 'Maestría'),
        ('D', 'Doctorado')
    )
    ETNIAS = (
        ('I', 'Indio Americano / Nativo de Alaska'),
        ('N', 'Negro / Afroamericano'),
        ('M', 'Mexicano / Americano'),
        ('B', 'Blanco'),
        ('A', 'Asiático'),
        ('P', 'Isleño del Pacífico / Hawaiano Nativo'),
        ('O', 'Otro'),
        ('NS', 'No lo sé'),
        )
    EDOCIVIL = (
        ('S', 'Soltero'),
        ('C', 'Casado'),
        ('D', 'Divorciado'),
        ('V', 'Viudo')
        )
    LABORAL = (
        ('M', 'Empleo de medio tiempo'),
        ('C', 'Empleo de tiempo completo'),
        ('D', 'Desempleado'),
        ('I', 'Trabaja por cuenta propia'),
        ('E', 'Estudiante'),
        ('R', 'Retirado')
        )
    paciente = models.OneToOneField(paciente, on_delete=models.CASCADE,
                                    related_name='generales')
    etnicidad = models.CharField(max_length=120, blank=True, choices=ETNIAS, verbose_name='Raza / Etnia')
    escolaridad = models.CharField(max_length=120, choices=ESCOLARIDADES, blank=True, verbose_name='Escolaridad (última terminada)')
    estadoCivil = models.CharField(max_length=120, blank=True, choices=EDOCIVIL, verbose_name='Estado Civil')
    situacionLaboral = models.CharField(max_length=120, blank=True, choices=LABORAL, verbose_name='Situación laboral actual')
    ocupacion = models.CharField(max_length=120, blank=True,  verbose_name='Ocupación')
    lugarTrabajo = models.CharField(max_length=120, blank=True, verbose_name='Lugar de trabajo')

    # calle = models.CharField(max_length=120, blank=True)
    # colonia = models.CharField(max_length=120, blank=True)
    # estado = models.CharField(max_length=120, blank=True)
    # cp = models.CharField(max_length=120, blank=True)
    # telefono = models.CharField(max_length=120, blank=True)


class cuestionario(models.Model):
    def __str__(self):
        return 'Paciente ' + str(self.id)

    paciente = models.OneToOneField(paciente, on_delete=models.CASCADE,
                                    related_name='cuestionarios')
    folio = models.IntegerField(blank=True, null=True)
    fechaCuestionario = models.DateField(null=True, verbose_name='Fecha del cuestionario')


class embarazo(models.Model):
    def __str__(self):
        return 'Paciente ' + str(self.id)

    paciente = models.OneToOneField(paciente, on_delete=models.CASCADE,
                                    related_name='embarazos')
    embarazo = models.CharField(max_length=10, choices=SiNo, blank=True, verbose_name='¿Está embarazada?')
    numerodeMeses = models.IntegerField(validators=[MinValueValidator(0),
                                        MaxValueValidator(10)], blank=True, null=True, verbose_name='Meses de embarazo')
    postparto = models.CharField(max_length=10, choices=SiNo, blank=True, verbose_name='¿Se encuentra en periodo de posparto?')
    mesesPostparto = models.IntegerField(blank=True, null=True, verbose_name='Meses desde el parto')


class viajes(models.Model):
    def __str__(self):
        return 'Paciente ' + str(self.id)

    paciente = models.OneToOneField(paciente, on_delete=models.CASCADE,
                                    related_name='viajes', blank=True)
    salioDelPais = models.CharField(max_length=10, choices=SiNo, blank=True,
                                    verbose_name='¿Realizó viajes al extranjero en los últimos 3 meses?')
    paicesVisitados = models.CharField(max_length=500, blank=True, verbose_name='En caso de ser sí su respuesta anterior, ¿qué países visitó?')
    fechaRegreso = models.DateField(verbose_name='¿En que fecha ingresó a México?',
                                    null=True, blank=True)

class sintomasCovid(models.Model):
    def __str__(self):
        return 'Paciente ' + str(self.id)

    paciente = models.OneToOneField(paciente, on_delete=models.CASCADE,
                                    related_name='sintomas')
    fiebre = models.CharField(max_length=10, choices=SiNo, blank=True)
    tos = models.CharField(max_length=10, choices=SiNo, blank=True)
    dolorArticular = models.CharField(max_length=10, choices=SiNo, blank=True, verbose_name='Dolor articular')
    dolorCabeza = models.CharField(max_length=10, choices=SiNo, blank=True, verbose_name='Dolor de cabeza')
    dolorToracico = models.CharField(max_length=10, choices=SiNo, blank=True, verbose_name='Dolor torácico')
    conjuntivitis = models.CharField(max_length=10, choices=SiNo, blank=True)
    dolorGarganta = models.CharField(max_length=10, choices=SiNo, blank=True, verbose_name='Dolor de garganta al tragar')
    # dolorAbdominal = models.CharField(max_length=10, choices=SiNo, blank=True)
    debilidad = models.CharField(max_length=10, choices=SiNo, blank=True)
    vomito = models.CharField(max_length=10, choices=SiNo, blank=True, verbose_name='Vómito')
    malestarGeneral = models.CharField(max_length=10, choices=SiNo, blank=True, verbose_name='Malestar general')
    dificltadRespirar = models.CharField(max_length=10, choices=SiNo, blank=True, verbose_name='Dificultad para respirar')
    perdidaGusto = models.CharField(max_length=10, choices=SiNo, blank=True, verbose_name='Pérdida del sentido del gusto')
    perdidaOlfato = models.CharField(max_length=10, choices=SiNo, blank=True, verbose_name='Pérdida del sentido del olfato')
    secrecionNasal = models.CharField(max_length=10, choices=SiNo, blank=True, verbose_name='Secreción nasal')
    otro = models.CharField(max_length=10, choices=SiNo, blank=True)
    irritabilidad = models.CharField(max_length=10, choices=SiNo, blank=True)
    escalofrios = models.CharField(max_length=10, choices=SiNo, blank=True, verbose_name='Escalofríos')

    cuantos = models.IntegerField(blank=True, null=True, verbose_name='¿Cuántos de estos síntomas ha presentado?')
    # cuales = models.CharField(max_length=300, blank=True)
    mejoria = models.CharField(max_length=10, choices=SiNo, blank=True,
                               verbose_name='¿Ha tenido mejoría en la presentación de los signos o síntomas?')
    fechaSintomas = models.DateField(verbose_name='Fecha de inicio de síntomas',
                                     null=True, blank=True)
    # sochechaCovid19 = models.CharField(max_length=10, choices=SiNo, blank=True)


class tratamientoCovid(models.Model):
    def __str__(self):
        return 'Paciente ' + str(self.id)

    paciente = models.OneToOneField(paciente, on_delete=models.CASCADE,
                                 related_name='tratamientos')
    tratamiento = models.CharField(max_length=10, choices=SiNo, blank=True,
                                   verbose_name='¿Desde el inicio de los signos/síntomas ha tomado algún tratamiento?')
    # quien = models.CharField(max_length=200, blank=True)


class medicamento(models.Model):
    #####
    # If this model changes, ensure to change it on the view to handle the post request
    def __str__(self):
        return 'Paciente ' + str(self.paciente.id) + ' medicamento ' + str(self.id)

    RUTAS = (
            ('OR', 'Oral'),
            ('IV', 'Intravenosa'),
            ('IM', 'Intramuscular'),
            ('OT', 'Otro'),
        )
    TIPO = (
        ('0', 'Antiviral'),
        ('1', 'Antibiotico'),
        ('2', 'Antiparacitario'),
        ('3', 'Antipirético'),
        ('4', 'Esteroideo'),
        ('5', 'Otro')
        )
    RECOMENDADORES = (
            ('0', 'Medico'),
            ('1', 'Familiar'),
            ('2', 'Vecino'),
            ('3', 'Amigo'),
            ('4', 'Automedicación'),
            ('5', 'Otro'),
        )

    paciente = models.ForeignKey(paciente, on_delete=models.CASCADE,
                                 related_name='medicamento')
    nombreMedicamento = models.CharField(max_length=200, blank=True, verbose_name='Nombre del medicamento', unique=True)
    tipo = models.CharField(max_length=200, blank=True, choices=TIPO)
    fechaInicio = models.DateField(blank=True, null=True, verbose_name='Fecha de inicio')
    dosis = models.CharField(max_length=200, blank=True)
    frecuencia = models.CharField(max_length=200, blank=True)
    ruta = models.CharField(max_length=15, choices=RUTAS, blank=True, verbose_name='Ruta de administración')
    fechaTermino = models.DateField(blank=True, null=True, verbose_name='Fecha de fin')
    quienIndico = models.CharField(max_length=15, choices=RECOMENDADORES, blank=True, verbose_name='¿Quién indicó el tratamiento?')


class antecedentesEpidimiologicos(models.Model):
    def __str__(self):
        return 'Paciente ' + str(self.id)
    RELACION = (
        ('0', 'Familiar'),
        ('1', 'Amigo'),
        ('2', 'Compañero de trabajo'),
        ('3', 'Pareja'),
        ('4', 'Otro'),
    )
    paciente = models.OneToOneField(paciente, on_delete=models.CASCADE,
                                    related_name='antecedentes', blank=True)
    contactoCovid = models.CharField(max_length=10, choices=SiNo, blank=True,
                                     verbose_name='¿Ha tenido contacto con alguna persona que tenga COVID-19 en las dos últimas semanas?')
    relacion = models.CharField(max_length=100, blank=True, choices=RELACION, verbose_name='¿Cuál es su relación con esta(s) persona(s)?')
    # quien = models.CharField(max_length=100, blank=True)
    viaje = models.CharField(max_length=10, choices=SiNo, blank=True, verbose_name='¿Realizó algún viaje en las últimas dos semanas?')
    pais = CountryField(verbose_name='Si su respuesta fue sí, especifique el lugar (país y ciudad)', blank=True)


class pruebas(models.Model):
    def __str__(self):
        return 'Paciente ' + str(self.id)

    PRUEBAS = (
            ('0', 'RT-PCR'),
            ('1', 'Prueba Rapida')
        )
    RESULTADOS = (
            ('P', 'Positivo'),
            ('N', 'Negativo'),
            ('I', 'Indeterminada')
        )
    paciente = models.OneToOneField(paciente, on_delete=models.CASCADE,
                                    related_name='pruebas')
    pruebas = models.CharField(max_length=10, choices=PRUEBAS, blank=True, verbose_name='Tipo de prueba realizada')
    fechaInicioPruebas = models.DateField(blank=True, null=True, verbose_name='Fecha de la prueba')
    resultadoPCR = models.CharField(max_length=10, choices=RESULTADOS, blank=True, verbose_name='Resultado de la prueba (RT-PCR)')
    resultadoRapida = models.CharField(max_length=10, choices=RESULTADOS, blank=True, verbose_name='Resultado de la prueba (Rápida)')
    igg = models.CharField(max_length=10, choices=RESULTADOS[0:2], blank=True, verbose_name='IgG')
    igm = models.CharField(max_length=10, choices=RESULTADOS[0:2], blank=True, verbose_name='IgM')


class seguridadSocial(models.Model):
    def __str__(self):
        return 'Paciente ' + str(self.id)

    SEGURIDAD = (
        ('0', 'IMSS'),
        ('1', 'ISSSTE'),
        ('2', 'PEMEX'),
        ('3', 'Defensa Nacional o Marina'),
        ('4', 'Seguro Popular'),
        ('5', 'Seguro Privado'),
        ('6', 'Otro'),
        ('7', 'Ninguno')
        )

    paciente = models.OneToOneField(paciente, on_delete=models.CASCADE,
                                    related_name='seguridadSocial')
    seguridad = models.CharField(max_length=10, choices=SEGURIDAD, blank=True, verbose_name='¿Qúe seguridad social tiene?')


class morbilidad(models.Model):
    def __str__(self):
        return 'Paciente ' + str(self.id)

    paciente = models.OneToOneField(paciente, on_delete=models.CASCADE,
                                    related_name='morbilidades')
    morbilidad = models.CharField(max_length=10, choices=SiNo, blank=True, verbose_name='¿Presenta alguna morbilidad?')
    diabetes = models.CharField(max_length=10, choices=SiNo, blank=True)
    epoc = models.CharField(max_length=10, choices=SiNo, blank=True, verbose_name='EPOC')
    obesidad = models.CharField(max_length=10, choices=SiNo, blank=True)
    asma = models.CharField(max_length=10, choices=SiNo, blank=True)
    inmunosupresion = models.CharField(max_length=10, choices=SiNo, blank=True, verbose_name='Inmunosupresión')
    cancer = models.CharField(max_length=10, choices=SiNo, blank=True, verbose_name='Cáncer')
    vih = models.CharField(max_length=10, choices=SiNo, blank=True, verbose_name='VIH/SIDA')
    tuberculosis = models.CharField(max_length=10, choices=SiNo, blank=True)
    insuficiencaiRenal = models.CharField(max_length=10, choices=SiNo, blank=True, verbose_name='Insuficiencia Renal')
    hipertension = models.CharField(max_length=10, choices=SiNo, blank=True, verbose_name='Hipertensión')
    trastornoNeurologico = models.CharField(max_length=10, choices=SiNo, blank=True, verbose_name='Transtorno Neurológico')
    cardiovascular = models.CharField(max_length=10, choices=SiNo, blank=True)
    otras = models.CharField(max_length=10, choices=SiNo, blank=True)
    cuales = models.CharField(max_length=500, blank=True, verbose_name='¿Cuáles?')

class habitosSaludables(models.Model):
    def __str__(self):
        return 'Paciente ' + str(self.id)

    ALCOHOL = (
        ('0', 'Ninguna'),
        ('1', '1 vez'),
        ('2', '2 veces'),
        ('3-5', '3-5 veces'),
        ('6-9', '6-9 veces'),
        ('10+', '10 o más')
        )

    CIGARRO = (
        ('No', 'No fumo'),
        ('1cs', 'Un cegarrillo por semana'),
        ('0.5s', 'Media cajetilla a la semana'),
        ('1s', 'Una cajetilla a la semana'),
        ('1-5d', '1 a 5 cigarrillos por día'),
        ('0.5d', 'Media cajetilla diaria'),
        ('1d', 'Una cajetilla al día')
        )
    DROGAS = (
        ('M', 'Marihuana'),
        ('C', 'Cocaína'),
        ('Me', 'Metanfetamina'),
        ('E', 'Éxtasis'),
        ('H', 'Heroína'),
        ('O', 'Otro'),
        )
    SINONOSE = (
        ('1', 'Si'),
        ('0', 'No'),
        ('3', 'No sé'),
    )

    paciente = models.OneToOneField(paciente, on_delete=models.CASCADE,
                                    related_name='habitos')
    frutas = models.CharField(max_length=10,  blank=True, verbose_name='¿Cuánta fruta come en un día común y corriente?(Tazas)')
    verduras = models.CharField(max_length=10,  blank=True, verbose_name='¿Cuánta verdura come en un día común y corriente?(Tazas)')
    pescado = models.CharField(max_length=10,  blank=True, choices=SINONOSE, verbose_name='¿Consume 100 gramos o mas de granos enteros al día?')
    granos = models.CharField(max_length=10,  blank=True, choices=SINONOSE, verbose_name='¿Consume 2 o más porciones de gra a la semana?')
    bebidasAzucar = models.CharField(max_length=10, blank=True, null=True, choices=SINONOSE, verbose_name='¿Bebe menos de 1 litro de bebidas azucaradas a la semana?')
    sal = models.CharField(max_length=10,  blank=True, choices=SINONOSE, verbose_name='Actualmente, ¿Está usted moderando o reduciendo su consumo de sal o sodio?')
    # carne = models.CharField(max_length=10,  blank=True)
    acitivadModerada = models.CharField(max_length=10,  blank=True, verbose_name='¿Cuánta actividad física moderada normalmente realiza semanalmente?')
    acitivadEnergetica = models.CharField(max_length=10,  blank=True, verbose_name='¿Cuánta actividad física enérgica/vigorosa realiza semanalmente?')
    fuma = models.CharField(max_length=10, choices=CIGARRO, blank=True, verbose_name='¿Con qué frecuencia fuma cigarrillos?')
    freqFumando = models.CharField(max_length=10, blank=True, verbose_name='Tiempo en años')
    indiceTabaquico = models.CharField(max_length=10, blank=True, verbose_name='Índice tabáquico')
    anosFumando = models.CharField(max_length=10, blank=True, verbose_name='¿Cuánto tiempo tiene fumando?')
    alcohol = models.CharField(max_length=10, choices=ALCOHOL, blank=True, verbose_name='En los útimos 30 días ¿Cuántas veces ha tomado por lo menos cinco bebidas alcohólicas seguidas?')
    drogas = models.CharField(max_length=10, choices=SiNo, blank=True, verbose_name='¿Ha consumido alguna sustancia nociva como marihuana,cocaína, mentafetamina, éxtasis?')
    cualddroga = models.CharField(max_length=10, choices=DROGAS, blank=True, verbose_name='Si su respuesta fue sí, especifique ¿Cuál?')
    otradroga = models.CharField(max_length=10, blank=True, verbose_name='¿Cuál otra droga?')
    # vasosAgua = models.IntegerField(blank=True, null=True)
    # horasSueno = models.CharField(max_length=10, blank=True)


class seguimiento(models.Model):
    def __str__(self):
        return 'Paciente ' + str(self.id)

    EVOLUCION = (
        ('T', 'En tratamiento'),
        ('H', 'Hospitalizado'),
        ('D', 'Defunción'),
        ('S', 'Seguimiento domiciliario'),
        ('R', 'Recuperado'),
    )
    INTENCIDAD = (
        ('A', 'Asintomatico'),
        ('M', 'Moderado'),
        ('L', 'Leve'),
        ('S', 'Severo'),
    )
    paciente = models.OneToOneField(paciente, on_delete=models.CASCADE,
                                    related_name='seguimiento')
    evolucion = models.CharField(max_length=10, choices=EVOLUCION, blank=True, verbose_name='Evolución de la enfermedad')
    fechaDefuncion = models.DateField(blank=True, null=True, verbose_name='En caso de defunción, fecha de defunción')
    fechaIngresoHospital = models.DateField(blank=True, null=True, verbose_name='En caso de hospitalización, fecha de ingreso')
    fechaEgresoHospital = models.DateField(blank=True, null=True, verbose_name='En caso de hospitalización, fecha de egreso')
    requiereOxigeno = models.CharField(max_length=10, choices=SiNo, blank=True, verbose_name='Requerimiento de oxígeno')
    requiereVentilacion = models.CharField(max_length=10, choices=SiNo, blank=True, verbose_name='Requerimiento de ventilación mecánica')
    complicacionHospital = models.CharField(max_length=10, choices=SiNo, blank=True, verbose_name='Complicaciones hospitalarias')
    cual = models.CharField(max_length=200, blank=True, verbose_name='¿Cuál?')
    intensidad = models.CharField(max_length=10, choices=INTENCIDAD, blank=True)