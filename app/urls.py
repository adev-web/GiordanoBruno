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
]
