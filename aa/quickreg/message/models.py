from django.db import models
from django.utils import timezone 
from users.models import CustomUser

class Message(models.Model):
	sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sender')
	receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='receiver')
	#sender = models.CharField(max_length=8) 
	#receiver = models.CharField(max_length=8)
	content = models.TextField() 
	subject = models.CharField(max_length=100)	
	timestamp = models.DateTimeField(default=timezone.now)
