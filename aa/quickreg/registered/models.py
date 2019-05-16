from django.db import models
from users.models import CustomUser
from courses.models import Courses

# Create your models here.
class Registered(models.Model):
	course_number=models.CharField(max_length=15, default='x')
	student=models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='student')

	@classmethod
	def create(cls, course_number, student):
		registered = cls(course_number=course_number, student=student)
		return registered

