from django.urls import path
from .import views

urlpatterns=[
	path('add_class_info/', views.add_class_info, name='add_class_info'),
	
]