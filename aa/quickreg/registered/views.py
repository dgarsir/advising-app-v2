from django.shortcuts import render_to_response, redirect, HttpResponse, render
from django.http import HttpResponse
from .models import Registered
from .models import Courses
from users.models import CustomUser
from appointments.models import Appointment
from django.db.models import Q


def add_class_info(request):
	courses = Courses.objects.all()
	reg = Registered.objects.all()
	num_courses = Courses.objects.all().count()
	curr_user = request.user
	if request.method == "POST":
		course_num = request.POST.get('course_select')
		new_registered = Registered.create(request.POST.get('course_select') ,curr_user)
		for _ in reg:
			if (_.student == curr_user) and (_.course_number == course_num):
				return redirect('already_registered')
		new_registered.save()
		return redirect('add_class_info')
	return render(request, 'add_class_info.html', {'courses': courses, 'num_courses': num_courses})

def already_registered(request):
	return render(request, 'already_registered.html')

def view_registered_courses(request):
	curr_user = request.user
	my_courses = list(Registered.objects.filter(student=curr_user))
	print(my_courses[0].course_number)
	print(curr_user)
	return render(request, 'view_registered_courses.html', {'my_courses': my_courses})