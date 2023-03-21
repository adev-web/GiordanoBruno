# IMPORTS!
import random
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db import connection
# MODELS
from .models import Estudiante, Inscription, Pago
from .forms import EstudianteForm, PagoForm, InscriptionForm

# TOOLS
from django.core.paginator import Paginator
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
        # url = f'create_inscription/{save_form.dni}'
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
        return redirect('list_pays', post_form.fk_inscription_id)


@login_required(login_url='signin')
def list_students(request):
    # FILTER_SQL
    if request.method == 'GET':
        consulta = f"SELECT dni, apellido_1, nombre_1, sexo, phone from app_estudiante;"
    else:
        query = request.POST.get('search_filter')
        consulta = f"SELECT dni, apellido_1, nombre_1, sexo, phone from app_estudiante where dni like '%{query}%';"
    # END_FILTER_SQL

    # SQL_CONNECTION
    sql_connection = connection.cursor()
    sql_connection.execute(consulta)
    result = sql_connection.fetchall()
    sql_connection.close()
    # END_SQL_CONNECTION
    # BLOCK_PAGINACION
    paginator = Paginator(result, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # END_PAGINACION

    if len(result) > 0:
        dictionary = {
            'tittle': 'Listado de Estudiantes',
            'labels': ('Cedula', 'Apellido', 'Nombre', 'Sexo', 'Telefono'),
            'items_data': page_obj,
            'redirect_url': 'opciones_estudiante',
        }
        return render(request, 'list_all.html', dictionary)
    else:
        dictionary = {
            'tittle': 'Creacion de Estudiante',
            'error': 'No existen estudiante registrados',
        }
        return redirect('create_students')


@login_required(login_url='signin')
def list_inscriptions(request, student_id):

    obj = get_object_or_404(Estudiante, pk=student_id)

    # FILTER_SQL
    if request.method == 'GET':
        consulta = f"select i.num_comprobante, i.date_year, i.curso, i.curso_nivel, i.trimestre from app_inscription as i inner join app_estudiante as e on i.fk_estudiante_id = e.dni and e.dni = '{student_id}';"
    else:
        query = request.POST.get('search_filter')
        consulta = f"select i.num_comprobante, i.date_year, i.curso, i.curso_nivel, i.trimestre from app_inscription as i inner join app_estudiante as e on i.fk_estudiante_id = e.dni and e.dni = '{student_id}' where i.num_comprobante like '%{query}%';"
    # END_FILTER_SQL

    # SQL_CONNECTION
    sql_connection = connection.cursor()
    sql_connection.execute(consulta)
    result = sql_connection.fetchall()
    sql_connection.close()
    # END_SQL_CONNECTION
    # BLOCK_PAGINACION
    paginator = Paginator(result, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # END_PAGINACION

    if len(result) > 0:
        dictionary = {
            'estudiante': f'{obj.apellido_1}, {obj.nombre_1}',
            'estudiante_dni': f'{obj.dni}',
            'tittle': 'Listado de Inscripciones',
            'labels': ('comprobante', 'año', 'curso', 'nivel del curso', 'trimestre'),
            'items_data': page_obj,
            'redirect_url': 'opciones_inscripcion',
        }
        return render(request, 'list_all.html', dictionary)
    else:
        return redirect('create_inscription', student_id)


@login_required(login_url='signin')
def list_pays(request, enrollment_id):
    obj = get_object_or_404(Inscription, pk=enrollment_id)
    # FILTER_SQL
    if request.method == 'GET':
        consulta = f"select factura_pago, cargo_tipo, monto_valor, monto_pagar, (monto_valor-monto_pagar) as saldo, fecha_pago from app_pago inner join app_inscription on fk_inscription_id = num_comprobante and num_comprobante = '{enrollment_id}';"
    else:
        query = request.POST.get('search_filter')
        consulta = f"select factura_pago, cargo_tipo, monto_valor, monto_pagar, (monto_valor-monto_pagar) as saldo, fecha_pago from app_pago inner join app_inscription on fk_inscription_id = num_comprobante and num_comprobante = '{enrollment_id}' where factura_pago like '%{query}%';"
    # END FILTER_SQL

    # SQL_CONNECTION
    sql_connection = connection.cursor()
    sql_connection.execute(consulta)
    result = sql_connection.fetchall()
    sql_connection.close()
    # END_SQL_CONNECTION
    # BLOCK_PAGINACION
    paginator = Paginator(result, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # END_PAGINACION

    if len(result) > 0:
        dictionary = {
            'estudiante': f'{obj.fk_estudiante.apellido_1}, {obj.fk_estudiante.nombre_1}',
            'estudiante_dni': f'{obj.fk_estudiante.dni}',
            'tittle': 'Listado de Pagos',
            'labels': ('Pago', 'tipo de cargo', 'Monto', 'Pagó', 'Saldo', 'Fecha de Pago', ),
            'items_data': page_obj,
            'redirect_url': 'opciones_pago',
        }
        return render(request, 'list_all.html', dictionary)
    else:
        return redirect('create_pay', enrollment_id)

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


def update_student(request, student_id):
    obj = get_object_or_404(Estudiante, pk=student_id)
    obj_form = EstudianteForm(instance=obj)
    if request.method == 'GET':
        dictionary = {
            'tittle': 'Actualizar Estudiante',
            'form': obj_form, }
        return render(request, 'form_create.html', dictionary)
    else:
        obj_form2 = EstudianteForm(request.POST, instance=obj)
        if obj_form2.is_valid():
            obj_form2.save()
            return redirect('list_students')
        else:
            dictionary = {
                'tittle': 'Actualizar Estudiante',
                'form': obj_form, }
            return render(request, 'form_create.html', dictionary)


def update_inscription(request, enrollment_id):
    obj = get_object_or_404(Inscription, pk=enrollment_id)
    obj_form = InscriptionForm(instance=obj)
    if request.method == 'GET':
        dictionary = {
            'tittle': 'Actualizar Inscripcion',
            'form': obj_form, }
        return render(request, 'form_create.html', dictionary)
    else:
        obj_form2 = InscriptionForm(request.POST, instance=obj)
        if obj_form2.is_valid():
            obj_form2.save()
            return redirect('list_inscriptions', obj.fk_estudiante.dni)
        else:
            dictionary = {
                'tittle': 'Actualizar Inscripcion',
                'form': obj_form, }
            return render(request, 'form_create.html', dictionary)


def update_pay(request, num_fact_id):
    obj = get_object_or_404(Pago, pk=num_fact_id)
    obj_form = PagoForm(instance=obj)
    if request.method == 'GET':
        dictionary = {
            'tittle': 'Actualizar Pago',
            'form': obj_form, }
        return render(request, 'form_create.html', dictionary)
    else:
        obj_form2 = PagoForm(request.POST, instance=obj)
        if obj_form2.is_valid():
            obj_form2.save()
            return redirect('list_pays', num_fact_id)
        else:
            dictionary = {
                'tittle': 'Actualizar Pago',
                'form': obj_form, }
            return render(request, 'form_create.html', dictionary)


def delete_student(request, student_id):
    obj = get_object_or_404(Estudiante, pk=student_id)
    obj.delete()
    return redirect('list_students')


def delete_inscription(request, enrollment_id):
    obj = get_object_or_404(Inscription, pk=enrollment_id)
    obj.delete()
    return redirect('list_inscriptions', enrollment_id)


def delete_pay(request, num_fact_id):
    obj = get_object_or_404(Pago, pk=num_fact_id)
    obj.delete()
    return redirect('opciones_pago', obj.fk_inscription.num_comprobante)
