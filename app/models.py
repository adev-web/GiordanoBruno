from django.db import models
import datetime
from .choices import GRUPOS_CHOICES, DISCAPACIDAD_CHOICES, SEXO_CHOICES, BLOQUE_CHOICES, CARGO_INSCRIPTIONS_CHOICES, TRIMESTRE_CHOICES


class Estudiante(models.Model):

    nombre_1 = models.CharField(
        verbose_name='primer nombre',
        blank=True,
        max_length=50)
    nombre_2 = models.CharField(
        verbose_name='segundo nombre',
        max_length=50,
        blank=True)
    apellido_1 = models.CharField(
        verbose_name='apellido paterno',
        blank=True,
        max_length=50)
    apellido_2 = models.CharField(
        verbose_name='apellido materno',
        max_length=50,
        blank=True)
    dni = models.CharField(
        verbose_name='documento de identificacion',
        max_length=20,
        primary_key=True,
        unique=True)
    sexo = models.CharField(
        blank=True,
        verbose_name='sexo',
        max_length=10,
        choices=SEXO_CHOICES,)
    fecha_nacimiento = models.DateField(
        blank=True, verbose_name='fecha de nacimiento',)
    email = models.EmailField(
        verbose_name='correo electronico',
        blank=True,
        max_length=50)
    phone = models.CharField(
        verbose_name='telefono',
        blank=True,
        max_length=20,
    )
    direccion = models.CharField(
        verbose_name='direccion de residencia',
        blank=True,
        max_length=250)
    discapacidad = models.CharField(
        verbose_name='discapacidad',
        blank=True,
        max_length=100,
        choices=DISCAPACIDAD_CHOICES,
        default='Ninguna')
    observaciones = models.TextField(
        verbose_name='observaciones generales',
        blank=True)
    def __str__(self):
        str = "{0}, {1} ({2})"
        return str.format(self.apellido_1, self.nombre_1, self.dni)

class Inscription(models.Model):

    fk_estudiante = models.ForeignKey(
        Estudiante,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name='estudiante',)

    num_comprobante = models.CharField(
        verbose_name='comprobante de matricula',
        primary_key=True,
        max_length=20,
        blank=True,)
    
    date_year = models.CharField(
        verbose_name='año',
        blank=True,
        max_length=4,
        default= datetime.datetime.now().year,
    )

    curso = models.CharField(
        choices=BLOQUE_CHOICES,
        default='Seleccione un Curso',
        verbose_name='Curso',
        max_length=30,)

    curso_nivel = models.CharField(
        choices=GRUPOS_CHOICES,
        default='Seleccione un nivel',
        verbose_name='nivel del curso',
        max_length=30,)

    trimestre = models.CharField(
        choices=TRIMESTRE_CHOICES,
        default='Opciones',
        verbose_name='trimestre',
        max_length=30,)
    def __str__(self):
        str = "{0} - {1} ({2})"
        return str.format(self.curso, self.curso_nivel, self.trimestre)


class Pago(models.Model):
    fk_inscription = models.ForeignKey(
        Inscription,
        blank=True,
        verbose_name='comprobante de matricula',
        on_delete=models.CASCADE,
    )
    factura_pago = models.CharField(
        verbose_name='comprobante de pago',
        primary_key=True,
        max_length=20,
        blank=True,)
    cargo_tipo = models.CharField(
        choices=CARGO_INSCRIPTIONS_CHOICES,
        default='Seleccione un nivel',
        verbose_name='Tipo de cargo',
        max_length=30)
    fecha_pago = models.DateField(
        default=datetime.date.today,
        verbose_name='fecha pago',)
    monto_valor = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name='Monto',)
    monto_pagar = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name='Recibido',)
    
    def __str__(self):
        str = "{0}, Saldo: Bl/.{1}"
        return str.format(self.factura_pago, self.monto_valor - self.monto_pagar,)
