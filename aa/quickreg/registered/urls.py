from django.urls import path
from .import views

urlpatterns=[
	path('add_class_info/', views.add_class_info, name='add_class_info'),
	path('already_registered/', views.already_registered, name='already_registered'),
	path('view_registered_courses/', views.view_registered_courses, name='view_registered_courses'),
]