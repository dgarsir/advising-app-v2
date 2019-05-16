from django.shortcuts import render_to_response, redirect, HttpResponse, render
from django.http import HttpResponse
from .models import Registered
from .models import Courses
from users.models import CustomUser
from appointments.models import Appointment


def add_class_info(request):
	courses = Courses.objects.all()
	curr_user = request.user
	if request.method == "POST":
		course_num = request.POST.get('course_select')
		print(course_num)
		new_registered = Registered.create(request.POST.get('course_select') ,curr_user)
		new_registered.save()
		return redirect('add_class_info')
	return render(request, 'add_class_info.html', {'courses': courses})

