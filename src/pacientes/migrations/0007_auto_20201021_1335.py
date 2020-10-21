# Generated by Django 3.1.1 on 2020-10-21 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0006_datosgralpaciente_paciente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datosgralpaciente',
            name='fechaIngresoDeExtrangero',
        ),
        migrations.AddField(
            model_name='paciente',
            name='fechaIngresoDeExtrangero',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de ingreso a México'),
        ),
        migrations.AlterField(
            model_name='datosgralpaciente',
            name='escolaridad',
            field=models.CharField(blank=True, choices=[('N', 'Ninguna'), ('P', 'Primaria'), ('S', 'Secundaria'), ('B', 'Bachillerato'), ('L', 'Licenciatura'), ('M', 'Maestría'), ('D', 'Doctorado')], max_length=120, verbose_name='Escolaridad (última terminada)'),
        ),
        migrations.AlterField(
            model_name='datosgralpaciente',
            name='estadoCivil',
            field=models.CharField(blank=True, choices=[('S', 'Soltero'), ('C', 'Casado'), ('D', 'Divorciado'), ('V', 'Viudo')], max_length=120, verbose_name='Estado Civil'),
        ),
        migrations.AlterField(
            model_name='datosgralpaciente',
            name='etnicidad',
            field=models.CharField(blank=True, choices=[('I', 'Indio Americano / Nativo de Alaska'), ('N', 'Negro / Afroamericano'), ('M', 'Mexicano / Americano'), ('B', 'Blanco'), ('A', 'Asiático'), ('P', 'Isleño del Pacífico / Hawaiano Nativo'), ('O', 'Otro'), ('NS', 'No lo sé')], max_length=120, verbose_name='Raza / Etina'),
        ),
        migrations.AlterField(
            model_name='datosgralpaciente',
            name='situacionLaboral',
            field=models.CharField(blank=True, choices=[('M', 'Empleo de medio tiempo'), ('C', 'Empleo de tiempo completo'), ('D', 'Desempleado'), ('I', 'Trabaja por cuenta propia'), ('E', 'Estudiante'), ('R', 'Retirado')], max_length=120, verbose_name='Situación laboral actual'),
        ),
    ]