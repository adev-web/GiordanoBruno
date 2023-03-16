#IMPORTS!
import random
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db import connection
##MODELS
from .models import Estudiante, Pago, Inscription
from .forms import EstudianteForm, PagoForm, InscriptionForm
# Create your views here.

@login_required(login_url='signin')
def main(request):
    dictionary = {'tittle': 'Main'}
    return render(request, 'inicio.html', dictionary)

@login_required(login_url='signin')
def create_student(request):
    if request.method == 'GET':
        dictionary = {
            'tittle': 'Creacion de Estudiante',
            'form': EstudianteForm(), }
        return render(request, 'form_create.html', dictionary)
    else:
        catch_form = EstudianteForm(request.POST)
        save_form = catch_form.save(commit=False)
        save_form.save()
        ##url = f'create_inscription/{save_form.dni}'
        return redirect('create_inscription', save_form.dni)

@login_required(login_url='signin')
def create_inscription(request, student_id):
    if request.method == 'GET':
        dictionary = {
            'tittle': 'Creacion de Inscripcion',
            'form': InscriptionForm, }
        return render(request, 'form_create.html', dictionary)
    else:
        consulta = Estudiante.objects.get(dni=student_id)
        form = InscriptionForm(request.POST)
        post_form = form.save(commit=False)
        post_form.fk_estudiante_id = consulta.pk
        post_form.num_comprobante = f'FMS-{random.randint(100, 999)}-{random.randint(100, 999)}'
        post_form.save()
        return redirect('create_pay', post_form.num_comprobante)

@login_required(login_url='signin')
def create_pay(request, enrollment_id):
    if request.method == 'GET':
        dictionary = {
            'tittle': 'Creacion de pago',
            'form': PagoForm, }
        return render(request, 'form_create.html', dictionary)
    else:
        form = PagoForm(request.POST)
        post_form = form.save(commit=False)
        post_form.fk_inscription_id = enrollment_id
        post_form.factura_pago = f'FPS-{random.randint(100, 999)}-{random.randint(100, 999)}'
        post_form.save()
        return redirect('list_pays', post_form.factura_pago)

@login_required(login_url='signin')
def list_students(request):
    cursor = connection.cursor()
    consulta = f'SELECT dni, apellido_1, nombre_1, sexo, phone from app_estudiante;'
    cursor.execute(consulta)
    result = cursor.fetchall()
    dictionary = {
        'tittle': 'Listado de Estudiantes',
        'labels': ('Cedula', 'Apellido', 'Nombre', 'Sexo', 'Telefono'),
        'items_data': result,
    }
    return render(request, 'list_students.html', dictionary)

@login_required(login_url='signin')
def list_inscriptions(request, student_id):
    try:
        cursor = connection.cursor()
        consulta = f"select i.num_comprobante, e.dni, e.apellido_1, e.nombre_1, i.curso, i.curso_nivel from app_inscription as i inner join app_estudiante as e on i.fk_estudiante_id = e.dni and e.dni = '{student_id}';"
        cursor.execute(consulta)
        result = cursor.fetchall()
        if len(result) != 0:
            dictionary = {
                'tittle': 'Listado de Inscripciones',
                'labels': ('comprobante', 'cedula', 'apellido', 'nombre', 'curso', 'nivel del curso'),
                'items_data': result, }
            return render(request, 'list_inscriptions.html', dictionary)
        else:
            return redirect('create_inscription', student_id)
    except:
        return redirect('create_inscription', student_id)

@login_required(login_url='signin')
def list_pays(request, enrollment_id):
    try:
        cursor = connection.cursor()
        consulta = f"select factura_pago, num_comprobante, cargo_tipo, monto_valor, monto_pagar, (monto_valor-monto_pagar) as saldo, fecha_pago from app_pago inner join app_inscription on fk_inscription_id = num_comprobante and num_comprobante = '{enrollment_id}';"
        cursor.execute(consulta)
        result = cursor.fetchall()
        dictionary = {
            'tittle': 'Listado de Pagos',
            'labels': ('Factura de Pago', 'Comprobante de matricula', 'tipo de cargo', 'Monto', 'Pagó', 'Saldo', 'Fecha de Pago', ),
            'items_data': result,
        }
        return render(request, 'list_pays.html', dictionary)
    except:
        dictionary = {
            'tittle': 'Listado de Pagos',
            'labels': ('Factura de Pago', 'Comprobante de matricula', 'tipo de cargo', 'Monto', 'Pagó', 'Saldo', 'Fecha de Pago', ),
            'error': 'Base de datos Vacia', }
        return render(request, 'list_pays.html', dictionary)

# Crea la funcion option_student que permita la visualizacion de las opciones delete

@login_required(login_url='signin')
def option_student(request, student_id):
    return render(request, 'options/student.html', {'id': student_id})

@login_required(login_url='signin')
def option_inscription(request, enrollment_id):
    return render(request, 'options/inscription.html', {'id': enrollment_id})

@login_required(login_url='signin')
def option_pays(request, num_fact):
    return render(request, 'options/pays.html', {'id': num_fact})
