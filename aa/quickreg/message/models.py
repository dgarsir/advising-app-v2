from django.db import models
from django.utils import timezone 

class Message(models.Model):
	sender = models.CharField(max_length=8)
	receiver = models.CharField(max_length=8)
	content = models.TextField() 
	subject = models.CharField(max_length=100)	
	timestamp = models.DateTimeField(default=timezone.now)

