from django.urls import path
from django.contrib import admin
from . import views

urlpatterns=[
	path('add_appointments/', views.add_appointment, name='add_appointment'),
	path('view_appointments/', views.view_appointments, name='view_appointments'),
	path('delete_appointment/', views.delete_appointment, name='delete_appointment'),
	path('request_appointment/', views.request_appointment, name='request_appointment'),
	path('appointment_summary/', views.appointment_summary, name='appointment_summary')
]