from django.urls import path
from . import views

urlpatterns=[
	path('courses/',views.courses_add,name='courses_add'),
	path('view_courses/', views.view_courses, name='view_courses'),
	path('del_course/', views.del_course, name='del_course')
]