from django.shortcuts import render_to_response, redirect, HttpResponse, render
from django.http import HttpResponse
from django.utils import timezone
from .models import Appointment
from .forms import AppointmentCreationForm
from .forms import List
from django.views.generic import ListView
from datetime import date
from users.models import CustomUser

def add_appointment(request):
    if request.method == "POST":
        form = AppointmentCreationForm(request.POST)
        if form.is_valid():
            a_form = form.save(commit=False)
            a_form.save()
            return redirect('view_appointments')
    else:
        form = AppointmentCreationForm()
    return render(request, 'add_appointment.html', {'form': form})

def view_appointments(request):
    if (request.user.user_type == 0):
       appoint=Appointment.objects.filter(customuser=request.user).order_by('date')
       appts=list(appoint)
       return render(request, 'view_appointments.html', {'appts':appts})
    else:
       appoint=Appointment.objects.all().order_by('date')
       appts=list(appoint)
       return render(request, 'view_appointments.html', {'appts':appts})  

def delete_appointment(request):
    apt = list(Appointment.objects.all())
    if request.method == "POST":
        Appointment.objects.filter(pk = request.POST.get('to_delete')).delete()
        return redirect('delete_appointment')
    return render(request, 'delete_appointment.html',{'apt': apt})


def request_appointment(request):
    req = list(Appointment.objects.filter(customuser=''))
    if request.method == "POST":
        selected = Appointment.objects.get(pk = request.POST.get('to_request'))
        selected.customuser = request.user
        selected.save()
        return redirect('home')
    return render(request, 'request_appointment.html',{'req': req})