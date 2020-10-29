# Generated by Django 3.1.1 on 2020-10-26 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0005_auto_20201026_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pruebas',
            name='fechaInicioPruebas',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de la prueba'),
        ),
        migrations.AlterField(
            model_name='seguimiento',
            name='fechaDefuncion',
            field=models.DateField(blank=True, null=True, verbose_name='En caso de defunción, fecha de defunción'),
        ),
    ]
