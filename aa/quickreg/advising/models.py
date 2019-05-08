from django.db import models
from django.utils import timezone
from users.models import CustomUser

# Create your models here.

majors = (
    ('Computer Science', 'CS'),
    ('Computer Engineering', 'CE')
)

semesters = (
    ('Fall 2019', 'Fall 2019'),
    ('Summer 2019', 'Summer 2019')
)

terms = (
    ('S', 'Summer 2019'),
    ('F', 'Fall 2019')
)

class Advising(models.Model):
    semester = models.CharField("Semester", max_length = 100,choices=semesters)
    major = models.CharField("Major", max_length = 100,choices=majors)
    QPA = models.CharField("QPA", max_length=100)
    GPA = models.CharField("GPA", max_length=100)
    intended_courses = models.TextField("Intended Courses")
    currently_enrolled = models.TextField("Currently Enrolled")
    completed_courses = models.TextField("Completed Courses")
    total_credits = models.PositiveIntegerField("Total Credits", default = 0)
    date_submitted = models.DateTimeField("Date Submitted", default=timezone.now)
    author = models.CharField("Author EMPLID", max_length=100, unique=True)
    status = models.IntegerField("Status", default = 0)