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
        return self.id

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
    escolaridad = models.CharField(max_length=120, choices=ESCOLARIDADES)
    etnicidad = models.CharField(max_length=120, blank=True)
    nacionalidad = CountryField()
    calle = models.CharField(max_length=120, blank=True)
    colonia = models.CharField(max_length=120, blank=True)
    estado = models.CharField(max_length=120, blank=True)
    cp = models.CharField(max_length=120, blank=True)
    telefono = models.CharField(max_length=120, blank=True)
    ocupacion = models.CharField(max_length=120, blank=True)


class cuestionario(models.Model):
    paciente = models.ForeignKey(paciente, on_delete=models.CASCADE,
                                 related_name='cuestioarios')
    folio = models.IntegerField()
    fechaCuestioario = models.DateField()    


class embarazo(models.Model):
    paciente = models.ForeignKey(paciente, on_delete=models.CASCADE,
                                 related_name='embarazos')
    embarazo = models.CharField(max_length=10, choices=SiNo)
    numerodeMeses = models.IntegerField(validators=[MinValueValidator(0),
                                        MaxValueValidator(9)])
    postparto = models.CharField(max_length=10, choices=SiNo)


class viajes(models.Model):
    paciente = models.ForeignKey(paciente, on_delete=models.CASCADE,
                                 related_name='viajes', blank=True)
    salioDelPais = models.CharField(max_length=10, choices=SiNo, blank=True)
    paicesVisitados = models.CharField(max_length=500, blank=True)
    fechaRegreso = models.DateField(verbose_name='Fecha de regreso a México',
                                    null=True)


class morbilidad(models.Model):
    paciente = models.ForeignKey(paciente, on_delete=models.CASCADE,
                                 related_name='morbilidades')
    morbilidad = models.CharField(max_length=10, choices=SiNo)
    diabetes = models.CharField(max_length=10, choices=SiNo)
    epoc = models.CharField(max_length=10, choices=SiNo)
    asma = models.CharField(max_length=10, choices=SiNo)
    inmunosupresion = models.CharField(max_length=10, choices=SiNo)
    vih = models.CharField(max_length=10, choices=SiNo)
    tuberculosis = models.CharField(max_length=10, choices=SiNo)
    insuficienciRenal = models.CharField(max_length=10, choices=SiNo)
    trastornoNeurologico = models.CharField(max_length=10, choices=SiNo)
    cardiovascular = models.CharField(max_length=10, choices=SiNo)
    obesidad = models.CharField(max_length=10, choices=SiNo)
    hipertension = models.CharField(max_length=10, choices=SiNo)
    cancer = models.CharField(max_length=10, choices=SiNo)
    otras = models.CharField(max_length=10, choices=SiNo)
    cuales = models.CharField(max_length=500)


class habitosSaludables(models.Model):
    paciente = models.ForeignKey(paciente, on_delete=models.CASCADE,
                                 related_name='habitos')
    frutas = models.CharField(max_length=10, choices=SiNo)
    vecesAzucar = models.IntegerField()
    carne = models.CharField(max_length=10, choices=SiNo)
    verduras = models.CharField(max_length=10, choices=SiNo)
    acitivad = models.CharField(max_length=10, choices=SiNo)
    vasosAgua = models.IntegerField()
    bebidasAzucar = models.CharField(max_length=10, choices=SiNo)
    horasSueno = models.CharField(max_length=10)
    fuma = models.CharField(max_length=10, choices=SiNo)
    cigarrosAlDia = models.IntegerField()
    alcohol = models.CharField(max_length=10, choices=SiNo)


class sintomasCovid(models.Model):
    paciente = models.ForeignKey(paciente, on_delete=models.CASCADE,
                                 related_name='sintomas')
    fiebre = models.CharField(max_length=10, choices=SiNo)
    tos = models.CharField(max_length=10, choices=SiNo)
    escalofrios = models.CharField(max_length=10, choices=SiNo)
    dolorCabeza = models.CharField(max_length=10, choices=SiNo)
    dolorToracico = models.CharField(max_length=10, choices=SiNo)
    dolorGarganta = models.CharField(max_length=10, choices=SiNo)
    dolorAbdominal = models.CharField(max_length=10, choices=SiNo)
    dolorArticular = models.CharField(max_length=10, choices=SiNo)
    debilidad = models.CharField(max_length=10, choices=SiNo)
    conjuntivitis = models.CharField(max_length=10, choices=SiNo)
    olfato = models.CharField(max_length=10, choices=SiNo)
    gusto = models.CharField(max_length=10, choices=SiNo)
    dificltadRespirar = models.CharField(max_length=10, choices=SiNo)
    irritabilidad = models.CharField(max_length=10, choices=SiNo)
    vomito = models.CharField(max_length=10, choices=SiNo)
    secrecionNasal = models.CharField(max_length=10, choices=SiNo)
    malestarGeneral = models.CharField(max_length=10, choices=SiNo)
    otras = models.CharField(max_length=10, choices=SiNo)
    cuales = models.CharField(max_length=300)
    mejoriaSintomas = models.CharField(max_length=10, choices=SiNo)
    sochechaCovid19 = models.CharField(max_length=10, choices=SiNo)


class tratamientoCovid(models.Model):
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
    paciente = models.ForeignKey(paciente, on_delete=models.CASCADE,
                                 related_name='tratamientos')
    tratamiento = models.CharField(max_length=10, choices=SiNo)
    quienIndico = models.CharField(max_length=15, choices=RECOMENDADORES)
    otro = models.CharField(max_length=200)
    nombreMedicamento = models.CharField(max_length=200)
    dosis = models.CharField(max_length=200)
    frecuencia = models.CharField(max_length=200)
    fechaInicio = models.DateField()
    fechaTermino = models.DateField()
    ruta = models.CharField(max_length=15, choices=RUTAS)


class antecedentesEpidimiologicos(models.Model):
    paciente = models.ForeignKey(paciente, on_delete=models.CASCADE,
                                 related_name='antecedentes')
    contactoCovid = models.CharField(max_length=10, choices=SiNo)
    relacion = models.CharField(max_length=100)
    viaje = models.CharField(max_length=10, choices=SiNo)
    ciudad = models.CharField(max_length=300)


class pruebas(models.Model):
    PRUEBAS = (
            (0, 'RT-PCR'),
            (1, 'Prueba Rapida')
        )
    RESULTADOS = (
            ('P', 'Positivo'),
            ('N', 'Negativo')
        )
    paciente = models.ForeignKey(paciente, on_delete=models.CASCADE,
                                 related_name='pruebas')
    pruebas = models.CharField(max_length=10, choices=SiNo)
    fechaSintomas = models.DateField()
    resultadoPCR = models.CharField(max_length=10, choices=RESULTADOS)
    igg = models.CharField(max_length=10, choices=RESULTADOS)
    igm = models.CharField(max_length=10, choices=RESULTADOS)
