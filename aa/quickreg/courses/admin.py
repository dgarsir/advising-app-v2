from django.contrib import admin
from .models import Courses

# Register your models here.
class CoursesAdmin(admin.ModelAdmin):
    pass
admin.site.register(Courses, CoursesAdmin)