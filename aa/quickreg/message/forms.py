from django import forms
from .models import Message 

class MessageCreationForm(forms.ModelForm):

	class Meta:
		model = Message 
		fields = (
			'receiver',
			'subject',
			'content',
		)
		labels = {
			'receiver' : 'To',
		}