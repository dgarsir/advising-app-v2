from django.db import models

# Create your models here.
terms=(
	('S','Summer 2019'),
	('F','Fall 2019')
	)

class Courses(models.Model):
    course_number=models.CharField(max_length=50)
    course_name=models.CharField(max_length=100)
    teacher=models.CharField(max_length=50)
    term=models.CharField(max_length=50,choices=terms)
    credits=models.PositiveIntegerField(default=0)
    

