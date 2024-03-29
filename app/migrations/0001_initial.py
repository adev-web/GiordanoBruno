# Generated by Django 4.1.2 on 2023-03-19 17:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('nombre_1', models.CharField(blank=True, max_length=50, verbose_name='primer nombre')),
                ('nombre_2', models.CharField(blank=True, max_length=50, verbose_name='segundo nombre')),
                ('apellido_1', models.CharField(blank=True, max_length=50, verbose_name='apellido paterno')),
                ('apellido_2', models.CharField(blank=True, max_length=50, verbose_name='apellido materno')),
                ('dni', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='documento de identificacion')),
                ('sexo', models.CharField(blank=True, choices=[('Opciones', 'Opciones'), ('Masculino', 'M'), ('Femenino', 'F')], default='Opciones', max_length=10, verbose_name='sexo')),
                ('fecha_nacimiento', models.DateField(blank=True, verbose_name='fecha de nacimiento')),
                ('email', models.EmailField(blank=True, max_length=50, verbose_name='correo electronico')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='telefono')),
                ('direccion', models.CharField(blank=True, max_length=250, verbose_name='direccion de residencia')),
                ('discapacidad', models.CharField(blank=True, choices=[('Ninguna', 'Ninguna'), ('Retardo', 'Retardo mental'), ('Auditiva', 'Discapacidad auditiva'), ('Visual', 'Discapacidad visual'), ('Generalizado', 'Trastorno generalizado del desarrollo (autismo, entre otros)'), ('Neuromotor', 'Trastorno neuromotor (parálisis cerebral, entre otros)'), ('Visual', 'Discapacidad visual')], default='Ninguna', max_length=100, verbose_name='discapacidad')),
                ('observaciones', models.TextField(blank=True, verbose_name='observaciones generales')),
            ],
        ),
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('num_comprobante', models.CharField(blank=True, max_length=20, primary_key=True, serialize=False, verbose_name='comprobante de matricula')),
                ('date_year', models.DateField(default=datetime.date.today, verbose_name='fecha de registro')),
                ('curso', models.CharField(choices=[('Opciones', 'Opciones'), ('PRIMER CICLO', 'PRIMER CICLO'), ('CIENCIAS', 'CIENCIAS'), ('COMERCIO', 'COMERCIO'), ('HUMANIDADES', 'HUMANIDADES'), ('INFORMATICA', 'INFORMATICA'), ('TURISMO', 'TURISMO')], default='Seleccione un Curso', max_length=30, verbose_name='Curso')),
                ('curso_nivel', models.CharField(choices=[('Opciones', 'Opciones'), ('7mo', 'Séptimo grado'), ('8vo', 'Octavo grado'), ('9no', 'Noveno grado'), ('10mo', 'Décimo grado'), ('11mo', 'Undécimo grado'), ('12mo', 'Duodecimo grado')], default='Seleccione un nivel', max_length=30, verbose_name='nivel del curso')),
                ('trimestre', models.CharField(choices=[('OPCIONES', 'OPCIONES'), ('PRIMER TRIMESTRE', 'I'), ('SEGUNDO TRIMESTRE', 'II'), ('TERCER TRIMESTRE', 'III')], default='Opciones', max_length=30, verbose_name='trimestre')),
                ('fk_estudiante', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.estudiante', verbose_name='estudiante')),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('factura_pago', models.CharField(blank=True, max_length=20, primary_key=True, serialize=False, verbose_name='comprobante de pago')),
                ('cargo_tipo', models.CharField(choices=[('Matricula', 'Matricula'), ('Mensualidad', 'Mensualidad')], default='Seleccione un nivel', max_length=30, verbose_name='Tipo de cargo')),
                ('fecha_pago', models.DateField(default=datetime.date.today, verbose_name='fecha pago')),
                ('monto_valor', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Monto')),
                ('monto_pagar', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Recibido')),
                ('fk_inscription', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.inscription', verbose_name='num_comprobante')),
            ],
        ),
    ]
