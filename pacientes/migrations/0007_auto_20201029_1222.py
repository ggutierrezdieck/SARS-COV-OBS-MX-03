# Generated by Django 3.1.1 on 2020-10-29 18:22

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0006_auto_20201026_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antecedentesepidimiologicos',
            name='pais',
            field=django_countries.fields.CountryField(blank=True, default='', max_length=2, verbose_name='Si su respuesta fue sí, especifique el lugar (país y ciudad)'),
            preserve_default=False,
        ),
    ]