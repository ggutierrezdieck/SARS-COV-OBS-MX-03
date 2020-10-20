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
    fechaNacimiento = models.DateField(verbose_name='Fecha de Nacimiento')
    sexo = models.CharField(max_length=120, choices=GENEROS)
    escolaridad = models.CharField(max_length=120, choices=ESCOLARIDADES, blank=True)
    etnicidad = models.CharField(max_length=120, blank=True)
    nacionalidad = CountryField()
    calle = models.CharField(max_length=120, blank=True)
    colonia = models.CharField(max_length=120, blank=True)
    estado = models.CharField(max_length=120, blank=True)
    cp = models.CharField(max_length=120, blank=True)
    telefono = models.CharField(max_length=120, blank=True)
    ocupacion = models.CharField(max_length=120, blank=True)


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


class viajes(models.Model):
    def __str__(self):
        return 'Paciente' + str(self.id)

    paciente = models.OneToOneField(paciente, on_delete=models.CASCADE,
                                    related_name='viajes', blank=True)
    salioDelPais = models.CharField(max_length=10, choices=SiNo, blank=True)
    paicesVisitados = models.CharField(max_length=500, blank=True)
    fechaRegreso = models.DateField(verbose_name='Fecha de regreso a México',
                                    null=True, blank=True)


class morbilidad(models.Model):
    def __str__(self):
        return 'Paciente' + str(self.id)

    paciente = models.OneToOneField(paciente, on_delete=models.CASCADE,
                                    related_name='morbilidades')
    morbilidad = models.CharField(max_length=10, choices=SiNo, blank=True)
    diabetes = models.CharField(max_length=10, choices=SiNo, blank=True)
    epoc = models.CharField(max_length=10, choices=SiNo, blank=True)
    asma = models.CharField(max_length=10, choices=SiNo, blank=True)
    inmunosupresion = models.CharField(max_length=10, choices=SiNo, blank=True)
    vih = models.CharField(max_length=10, choices=SiNo, blank=True)
    tuberculosis = models.CharField(max_length=10, choices=SiNo, blank=True)
    insuficienciRenal = models.CharField(max_length=10, choices=SiNo, blank=True)
    trastornoNeurologico = models.CharField(max_length=10, choices=SiNo, blank=True)
    cardiovascular = models.CharField(max_length=10, choices=SiNo, blank=True)
    obesidad = models.CharField(max_length=10, choices=SiNo, blank=True)
    hipertension = models.CharField(max_length=10, choices=SiNo, blank=True)
    cancer = models.CharField(max_length=10, choices=SiNo, blank=True)
    otras = models.CharField(max_length=10, choices=SiNo, blank=True)
    cuales = models.CharField(max_length=500, blank=True)


class habitosSaludables(models.Model):
    def __str__(self):
        return 'Paciente' + str(self.id)

    paciente = models.OneToOneField(paciente, on_delete=models.CASCADE,
                                    related_name='habitos')
    frutas = models.CharField(max_length=10, choices=SiNo, blank=True)
    vecesAzucar = models.IntegerField(blank=True, null=True)
    carne = models.CharField(max_length=10, choices=SiNo, blank=True)
    verduras = models.CharField(max_length=10, choices=SiNo, blank=True)
    acitivad = models.CharField(max_length=10, choices=SiNo, blank=True)
    vasosAgua = models.IntegerField(blank=True, null=True)
    bebidasAzucar = models.CharField(max_length=10, choices=SiNo, blank=True)
    horasSueno = models.CharField(max_length=10, blank=True)
    fuma = models.CharField(max_length=10, choices=SiNo, blank=True)
    cigarrosAlDia = models.IntegerField(blank=True, null=True)
    alcohol = models.CharField(max_length=10, choices=SiNo, blank=True)


class sintomasCovid(models.Model):
    def __str__(self):
        return 'Paciente' + str(self.id)

    paciente = models.OneToOneField(paciente, on_delete=models.CASCADE,
                                    related_name='sintomas')
    fiebre = models.CharField(max_length=10, choices=SiNo, blank=True)
    tos = models.CharField(max_length=10, choices=SiNo, blank=True)
    escalofrios = models.CharField(max_length=10, choices=SiNo, blank=True)
    dolorCabeza = models.CharField(max_length=10, choices=SiNo, blank=True)
    dolorToracico = models.CharField(max_length=10, choices=SiNo, blank=True)
    dolorGarganta = models.CharField(max_length=10, choices=SiNo, blank=True)
    dolorAbdominal = models.CharField(max_length=10, choices=SiNo, blank=True)
    dolorArticular = models.CharField(max_length=10, choices=SiNo, blank=True)
    debilidad = models.CharField(max_length=10, choices=SiNo, blank=True)
    conjuntivitis = models.CharField(max_length=10, choices=SiNo, blank=True)
    olfato = models.CharField(max_length=10, choices=SiNo, blank=True)
    gusto = models.CharField(max_length=10, choices=SiNo, blank=True)
    dificltadRespirar = models.CharField(max_length=10, choices=SiNo, blank=True)
    irritabilidad = models.CharField(max_length=10, choices=SiNo, blank=True)
    vomito = models.CharField(max_length=10, choices=SiNo, blank=True)
    secrecionNasal = models.CharField(max_length=10, choices=SiNo, blank=True)
    malestarGeneral = models.CharField(max_length=10, choices=SiNo, blank=True)
    otras = models.CharField(max_length=10, choices=SiNo, blank=True)
    cuales = models.CharField(max_length=300, blank=True)
    mejoriaSintomas = models.CharField(max_length=10, choices=SiNo, blank=True)
    sochechaCovid19 = models.CharField(max_length=10, choices=SiNo, blank=True)


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
            ('O', 'Oral'),
            ('IV', 'Intravenosa'),
            ('IM', 'Intramuscular'),
            ('O', 'Otro'),
        )
    paciente = models.OneToOneField(paciente, on_delete=models.CASCADE,
                                    related_name='tratamientos')
    tratamiento = models.CharField(max_length=10, choices=SiNo, blank=True)
    quienIndico = models.CharField(max_length=15, choices=RECOMENDADORES, blank=True)
    otro = models.CharField(max_length=200, blank=True)
    nombreMedicamento = models.CharField(max_length=200, blank=True)
    dosis = models.CharField(max_length=200, blank=True)
    frecuencia = models.CharField(max_length=200, blank=True)
    fechaInicio = models.DateField(blank=True, null=True)
    fechaTermino = models.DateField(blank=True, null=True)
    ruta = models.CharField(max_length=15, choices=RUTAS, blank=True)


class antecedentesEpidimiologicos(models.Model):
    def __str__(self):
        return 'Paciente' + str(self.id)

    paciente = models.OneToOneField(paciente, on_delete=models.CASCADE,
                                    related_name='antecedentes', blank=True)
    contactoCovid = models.CharField(max_length=10, choices=SiNo, blank=True)
    relacion = models.CharField(max_length=100, blank=True)
    viaje = models.CharField(max_length=10, choices=SiNo, blank=True)
    ciudad = models.CharField(max_length=300, blank=True)


class pruebas(models.Model):
    def __str__(self):
        return 'Paciente' + str(self.id)

    PRUEBAS = (
            (0, 'RT-PCR'),
            (1, 'Prueba Rapida')
        )
    RESULTADOS = (
            ('P', 'Positivo'),
            ('N', 'Negativo')
        )
    paciente = models.OneToOneField(paciente, on_delete=models.CASCADE,
                                    related_name='pruebas')
    pruebas = models.CharField(max_length=10, choices=SiNo, blank=True)
    fechaSintomas = models.DateField(blank=True, null=True)
    resultadoPCR = models.CharField(max_length=10, choices=RESULTADOS, blank=True)
    igg = models.CharField(max_length=10, choices=RESULTADOS, blank=True)
    igm = models.CharField(max_length=10, choices=RESULTADOS, blank=True)


class seguimiento(models.Model):
    def __str__(self):
        return 'Paciente' + str(self.id)

    EVOLUCION = (
        ('T', 'En tratamiento'),
        ('H', 'Hospitalizado'),
        ('D', 'Defuncion'),
        ('S', 'Seguimiento domicilario'),
        ('R', 'Recuperado'),
    )
    INTENCIDAD = (
        ('A', 'Asintomatico'),
        ('M', 'Moderado'),
        ('L', 'Leve'),
        ('S', 'Severo'),
    )
    evolucion = models.CharField(max_length=10, choices=EVOLUCION, blank=True)
    fechaDefuncion = models.DateField(blank=True, null=True)
    fechaIngresoHospital = models.DateField(blank=True, null=True)
    fechaEgresoHospital = models.DateField(blank=True, null=True)
    requiereOxigeno = models.CharField(max_length=10, choices=SiNo, blank=True)
    requiereVentilacion = models.CharField(max_length=10, choices=SiNo, blank=True)
    complicacionHospital = models.CharField(max_length=10, choices=SiNo, blank=True)
    cual = models.CharField(max_length=200, blank=True)
    intensidad = models.CharField(max_length=10, choices=INTENCIDAD, blank=True)
