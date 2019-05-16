from django.shortcuts import render_to_response, redirect, HttpResponse, render
from django.http import HttpResponse
from django.utils import timezone
from .models import Appointment
from .forms import AppointmentCreationForm
from .forms import List
from django.views.generic import ListView
from datetime import date, datetime
import datetime
from users.models import CustomUser
from django.db.models import Count, Q
from django.utils import timezone
from django.db.models.functions import ExtractMonth, TruncMonth, ExtractYear, ExtractDay

def add_appointment(request):
    if request.method == "POST":
        form = AppointmentCreationForm(request.POST)
        if form.is_valid():
            a_form = form.save(commit=False)
            a_form.save()
            print(a_form.customuser)
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
       for appt in appts:
           print(appt.customuser.last_name)
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

def appointment_summary(request):
    day=Appointment.objects.annotate(day=ExtractDay('date')).values('date').annotate(Count=Count('id'))
    month=Appointment.objects.annotate(month=ExtractMonth('date')).values('month').annotate(Count=Count('id'))
    year=Appointment.objects.annotate(year=ExtractYear('date')).values('year').annotate(Count=Count('id'))
    fall=Appointment.objects.filter(date__range=['2019-09-01', '2019-12-22']).annotate(month=ExtractMonth('date')).values('month').annotate(Count=Count('id'))
    spring=Appointment.objects.filter(date__range=['2019-02-01', '2019-05-29']).annotate(month=ExtractMonth('date')).values('month').annotate(Count=Count('id'))
    return render(request, 'appointment_summary.html', {'day':day, 'fall':fall, 'month':month, 'year':year, 'spring':spring})

