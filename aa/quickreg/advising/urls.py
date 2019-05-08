from django.urls import path

from . import views

urlpatterns = [
    path('select_advising/', views.select_advising, name='select_advising'),
    path('submit/', views.submit_advising, name='submit_advising'),
    path('view/', views.view_advising, name='view_advising'),
    path('view_faculty/', views.view_advising_faculty, name='view_advising_faculty'),
    path('confirm/', views.confirm_approve, name='confirm_approve'),
    path('deny/', views.confirm_deny, name='confirm_deny')
]