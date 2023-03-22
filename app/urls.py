from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('crear/estudiante/', views.create_student, name='create_students'),
    path('crear/estudiante/inscription/id/<str:student_id>/', views.create_inscription, name='create_inscription'),
    path('crear/estudiante/inscription/pago/id/<str:enrollment_id>/', views.create_pay, name='create_pay'),

    path('listado/estudiantes/', views.list_students, name='list_students'),
    path('listado/inscripciones/id/<str:student_id>/', views.list_inscriptions, name='list_inscriptions'),
    path('listado/pagos/id/<str:enrollment_id>/', views.list_pays, name='list_pays'),

    path('opciones/estudiante/id/<str:student_id>/', views.option_student, name='opciones_estudiante'),
    path('opciones/inscripcion/id/<str:enrollment_id>/', views.option_inscription, name='opciones_inscripcion'),
    path('opciones/pago/id/<str:num_fact>/', views.option_pays, name='opciones_pago'),

    path('update/estudiante/id/<str:student_id>/', views.update_student, name='update_student'),
    path('update/inscripcion/id/<str:enrollment_id>/', views.update_inscription, name='update_inscription'),
    path('update/pago/id/<str:num_fact_id>/', views.update_pay, name='update_pay'),

    path('delete/estudiante/id/<str:student_id>/', views.delete_student, name='delete_student'),
    path('delete/inscripcion/id/<str:enrollment_id>/', views.delete_inscription, name='delete_inscription'),
    path('delete/pago/id/<str:num_fact_id>/', views.delete_pay, name='delete_pay'),

    path('print/pago/id/<str:num_fact_id>/', views.pay_x_inscription, name='print_fact'),
    ## agregar abono
    path('agregar/pago/abono/id/<str:num_pass_id>/', views.add_pass, name='add_pass'),
]
