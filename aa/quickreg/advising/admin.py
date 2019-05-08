from django.contrib import admin
from .models import Advising

# Register your models here.
class AdvisingAdmin(admin.ModelAdmin):
    pass
admin.site.register(Advising, AdvisingAdmin)