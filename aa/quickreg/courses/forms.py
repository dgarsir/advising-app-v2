from django import forms
from .models import Courses

class AddClassForms(forms.ModelForm):
	class Meta:
		model= Courses
		fields=(
			'course_number', 
			'course_name',
			'teacher',
			'term', 
			'credits'
			)