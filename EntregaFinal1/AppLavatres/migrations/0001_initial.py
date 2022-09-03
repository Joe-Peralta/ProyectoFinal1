# Generated by Django 3.2.6 on 2022-09-03 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_animal', models.CharField(max_length=30)),
                ('nombre_duenio', models.CharField(max_length=30)),
                ('corte_pelo', models.BooleanField()),
                ('fecha_turno', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Indumentaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_indumentaria', models.CharField(max_length=40)),
                ('ropa_banca', models.BooleanField()),
                ('nombre_cliente', models.CharField(max_length=30)),
                ('fecha_retiro', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_vehiculo', models.CharField(max_length=30)),
                ('aspirado', models.BooleanField()),
                ('dominio', models.CharField(max_length=7)),
                ('ingreso', models.DateTimeField()),
                ('egreso', models.DateTimeField()),
            ],
        ),
    ]
