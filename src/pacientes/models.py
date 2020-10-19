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
        return 'Paciente' + str(self.id)

    ESCOLARIDADES = (
        ('N', 'Ninguna'),
        ('P', 'Primaria'),
        ('S', 'Secundaria'),
        ('B', 'Bachillerato'),
        ('L', 'Licenciatura'),
        ('M', 'Maestría'),
        ('D', 'Doctorado')
    )
    GENEROS = (
        ('H', 'Hombre'),
        ('M', 'Mujer')
    )
    ETNIAS = (
        ('I', 'Indio Americano / Nativo de Alasca'),
        ('N', 'Negro / Afroamericano'),
        ('M', 'Mexicano/Americano'),
        ('B', 'Blanco'),
        ('A', 'Asiático'),
        ('P', 'Isleño del Pacífico / Hawaiano'),
        ('O', 'Otro'),
        ('NS', 'No lo sé'),
        )
    EDOCIVIL = (
        ('S', 'Soltero'),
        ('C', 'Casado'),
        ('D', 'Divorsiado'),
        ('V', 'Viudo')
        )
    LABORAL = (
        ('M', 'Empleo de medio tiempo'),
        ('C', 'Empleo de tiempo completo'),
        ('D', 'Desempleo'),
        ('M', 'Empleo de medio tiempo'),
        ('I', 'Trabaja por cuenta propia'),
        ('E', 'Estudiante'),
        ('R', 'Retirado')
        )
    fechaNacimiento = models.DateField(verbose_name='Fecha de Nacimiento')
    sexo = models.CharField(max_length=120, choices=GENEROS)
    escolaridad = models.CharField(max_length=120, choices=ESCOLARIDADES, blank=True)
    etnicidad = models.CharField(max_length=120, blank=True, choices=ETNIAS)
    nacionalidad = CountryField()
    fechaIngresoDeExtrangero = models.DateField(verbose_name='Fecha de ingreso a México')
    # calle = models.CharField(max_length=120, blank=True)
    # colonia = models.CharField(max_length=120, blank=True)
    estado = models.CharField(max_length=120, blank=True)
    # cp = models.CharField(max_length=120, blank=True)
    # telefono = models.CharField(max_length=120, blank=True)
    ocupacion = models.CharField(max_length=120, blank=True)
    estadoCivil = models.CharField(max_length=120, blank=True, choices=EDOCIVIL)
    situacionLaboral = models.CharField(max_length=120, blank=True, choices=LABORAL)
    ocupacion = models.CharField(max_length=120, blank=True)
    lugarTrabajo = models.CharField(max_length=120, blank=True)


class cuestionario(models.Model):
    def __str__(self):
        return 'Paciente' + str(self.id)

    paciente = models.OneToOneField(paciente, on_delete=models.CASCADE,
                                    related_name='cuestioarios')
    folio = models.IntegerField(blank=True, null=True)
    fechaCuestioario = models.DateField(null=True)


class embarazo(models.Model):
    def __str__(self):
        return 'Paciente' + str(self.id)

    paciente = models.OneToOneField(paciente, on_delete=models.CASCADE,
                                    related_name='embarazos')
    embarazo = models.CharField(max_length=10, choices=SiNo, blank=True)
    numerodeMeses = models.IntegerField(validators=[MinValueValidator(0),
                                        MaxValueValidator(9)], blank=True, null=True)
    postparto = models.CharField(max_length=10, choices=SiNo, blank=True)
    mesesPostparto = models.IntegerField(validators=[MinValueValidator(0),
                                        MaxValueValidator(9)], blank=True, null=True)

class viajes(models.Model):
    def __str__(self):
        return 'Paciente' + str(self.id)

    paciente = models.OneToOneField(paciente, on_delete=models.CASCADE,
                                    related_name='viajes', blank=True)
    salioDelPais = models.CharField(max_length=10, choices=SiNo, blank=True)
    paicesVisitados = models.CharField(max_length=500, blank=True)
    fechaRegreso = models.DateField(verbose_name='Fecha de regreso a México',
                                    null=True, blank=True)

class sintomasCovid(models.Model):
    def __str__(self):
        return 'Paciente' + str(self.id)

    paciente = models.OneToOneField(paciente, on_delete=models.CASCADE,
                                    related_name='sintomas')
    fiebre = models.CharField(max_length=10, choices=SiNo, blank=True)
    tos = models.CharField(max_length=10, choices=SiNo, blank=True)
    dolorArticular = models.CharField(max_length=10, choices=SiNo, blank=True)
    dolorCabeza = models.CharField(max_length=10, choices=SiNo, blank=True)
    dolorToracico = models.CharField(max_length=10, choices=SiNo, blank=True)
    conjuntivitis = models.CharField(max_length=10, choices=SiNo, blank=True)
    dolorGarganta = models.CharField(max_length=10, choices=SiNo, blank=True)
    # dolorAbdominal = models.CharField(max_length=10, choices=SiNo, blank=True)
    debilidad = models.CharField(max_length=10, choices=SiNo, blank=True)
    vomito = models.CharField(max_length=10, choices=SiNo, blank=True)
    malestarGeneral = models.CharField(max_length=10, choices=SiNo, blank=True)
    dificltadRespirar = models.CharField(max_length=10, choices=SiNo, blank=True)
    perdidaGusto = models.CharField(max_length=10, choices=SiNo, blank=True)
    perdidaOlfato = models.CharField(max_length=10, choices=SiNo, blank=True)
    secrecionNasal = models.CharField(max_length=10, choices=SiNo, blank=True)
    otras = models.CharField(max_length=10, choices=SiNo, blank=True)
    irritabilidad = models.CharField(max_length=10, choices=SiNo, blank=True)
    escalofrios = models.CharField(max_length=10, choices=SiNo, blank=True)

    cuantos = models.IntegerField(blank=True, null=True)
    # cuales = models.CharField(max_length=300, blank=True)
    # mejoriaSintomas = models.CharField(max_length=10, choices=SiNo, blank=True)
    fechaSintomas = models.DateField(verbose_name='Fecha de inicio de síntomas',
                                     null=True, blank=True)
    # sochechaCovid19 = models.CharField(max_length=10, choices=SiNo, blank=True)


class tratamientoCovid(models.Model):
    def __str__(self):
        return 'Paciente' + str(self.id)

    RECOMENDADORES = (
            (0, 'Medico'),
            (1, 'Familiar'),
            (2, 'Vecino'),
            (3, 'Amigo'),
            (4, 'Automedicación'),
            (5, 'Otro'),
        )
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
    paciente = models.ForeignKey(paciente, on_delete=models.CASCADE,
                                 related_name='tratamientos')
    tratamiento = models.CharField(max_length=10, choices=SiNo, blank=True)
    nombreMedicamento = models.CharField(max_length=200, blank=True)
    tipo = models.CharField(max_length=200, blank=True, choices=TIPO)
    fechaInicio = models.DateField(blank=True, null=True)
    dosis = models.CharField(max_length=200, blank=True)
    frecuencia = models.CharField(max_length=200, blank=True)
    ruta = models.CharField(max_length=15, choices=RUTAS, blank=True)
    fechaTermino = models.DateField(blank=True, null=True)
    quienIndico = models.CharField(max_length=15, choices=RECOMENDADORES, blank=True)
    quien = models.CharField(max_length=200, blank=True)


class antecedentesEpidimiologicos(models.Model):
    def __str__(self):
        return 'Paciente' + str(self.id)
    RELACION = (
        (0, 'Familiar'),
        (1, 'Amigo'),
        (2, 'Compañero de trabajo'),
        (3, 'Pareja'),
        (4, 'Otro'),
    )
    paciente = models.OneToOneField(paciente, on_delete=models.CASCADE,
                                    related_name='antecedentes', blank=True)
    contactoCovid = models.CharField(max_length=10, choices=SiNo, blank=True)
    relacion = models.CharField(max_length=100, blank=True)
    quien = models.CharField(max_length=100, blank=True)
    viaje = models.CharField(max_length=10, choices=SiNo, blank=True)
    pais = CountryField()


class pruebas(models.Model):
    def __str__(self):
        return 'Paciente' + str(self.id)

    PRUEBAS = (
            (0, 'RT-PCR'),
            (1, 'Prueba Rapida')
        )
    RESULTADOS = (
            ('P', 'Positivo'),
            ('N', 'Negativo'),
            ('I', 'Indeterminada')
        )
    paciente = models.OneToOneField(paciente, on_delete=models.CASCADE,
                                    related_name='pruebas')
    pruebas = models.CharField(max_length=10, choices=SiNo, blank=True)
    fechaSintomas = models.DateField(blank=True, null=True)
    resultadoPCR = models.CharField(max_length=10, choices=RESULTADOS, blank=True)
    igg = models.CharField(max_length=10, choices=RESULTADOS[0:1], blank=True)
    igm = models.CharField(max_length=10, choices=RESULTADOS[0:1], blank=True)


class seguridadSocial(models.Model):
    def __str__(self):
        return 'Paciente' + str(self.id)

    SEGURIDAD = (
        ('0', 'IMSS'),
        ('1', 'ISSSTE'),
        ('2', 'PEMEX'),
        ('3', 'Defensa Nacional o Marina'),
        ('4', 'Seguro Popular'),
        ('5', 'Seguro Privado'),
        ('6', 'Otro'),
        ('7', 'Ninbguno')
        )

    paciente = models.OneToOneField(paciente, on_delete=models.CASCADE,
                                    related_name='seguridadSocial')
    seguridad = models.CharField(max_length=10, choices=SEGURIDAD , blank=True)


class morbilidad(models.Model):
    def __str__(self):
        return 'Paciente' + str(self.id)

    paciente = models.OneToOneField(paciente, on_delete=models.CASCADE,
                                    related_name='morbilidades')
    morbilidad = models.CharField(max_length=10, choices=SiNo, blank=True)
    diabetes = models.CharField(max_length=10, choices=SiNo, blank=True)
    epoc = models.CharField(max_length=10, choices=SiNo, blank=True)
    obesidad = models.CharField(max_length=10, choices=SiNo, blank=True)
    asma = models.CharField(max_length=10, choices=SiNo, blank=True)
    inmunosupresion = models.CharField(max_length=10, choices=SiNo, blank=True)
    cancer = models.CharField(max_length=10, choices=SiNo, blank=True)
    vih = models.CharField(max_length=10, choices=SiNo, blank=True)
    tuberculosis = models.CharField(max_length=10, choices=SiNo, blank=True)
    otras = models.CharField(max_length=10, choices=SiNo, blank=True)
    insuficienciRenal = models.CharField(max_length=10, choices=SiNo, blank=True)
    hipertension = models.CharField(max_length=10, choices=SiNo, blank=True)
    cuales = models.CharField(max_length=500, blank=True)
    trastornoNeurologico = models.CharField(max_length=10, choices=SiNo, blank=True)
    cardiovascular = models.CharField(max_length=10, choices=SiNo, blank=True)


class habitosSaludables(models.Model):
    def __str__(self):
        return 'Paciente' + str(self.id)

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

    paciente = models.OneToOneField(paciente, on_delete=models.CASCADE,
                                    related_name='habitos')
    frutas = models.CharField(max_length=10,  blank=True)
    verduras = models.CharField(max_length=10,  blank=True)
    pescado = models.CharField(max_length=10,  blank=True)
    granos = models.CharField(max_length=10,  blank=True)
    bebidasAzucar = models.IntegerField(blank=True, null=True)
    sal = models.CharField(max_length=10,  blank=True)
    # carne = models.CharField(max_length=10,  blank=True)
    acitivadModerada = models.CharField(max_length=10,  blank=True)
    acitivadEnergetica = models.CharField(max_length=10,  blank=True)
    fuma = models.CharField(max_length=10, choices=CIGARRO, blank=True)
    anosFumando = models.CharField(max_length=10, blank=True)
    indiceTabaquico = models.CharField(max_length=10, blank=True)
    alcohol = models.CharField(max_length=10,choices=ALCOHOL, blank=True)
    # vasosAgua = models.IntegerField(blank=True, null=True)
    # horasSueno = models.CharField(max_length=10, blank=True)


class seguimeinto(models.Model):
    def __str__(self):
        return 'Paciente' + str(self.id)

    paciente = models.OneToOneField(paciente, on_delete=models.CASCADE,
                                    related_name='seguimeinto')
