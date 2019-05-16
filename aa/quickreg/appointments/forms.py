from django import forms
from .models import Appointment
from django.forms.fields import ChoiceField

class AppointmentCreationForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = (
            'date', 
            'start_time', 
            'end_time'
        )
class List(forms.ModelForm):
    class Meta:
        model=Appointment
        fields= (
            'date',
            'start_time',
            'end_time'
            )
class List(forms.Form):
    req_fields= ('date','start_time','end_time')
    req=forms.ChoiceField(choices=req_fields)
''''''

