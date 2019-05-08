from django.db import models
from django.utils import timezone
from users.models import CustomUser

class Appointment(models.Model):
	date=models.DateField(default=timezone.localdate)
	start_time=models.TimeField(default=timezone.now)
	end_time=models.TimeField(default=timezone.now)
	customuser = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default='')

	def _str_(self):
		return str(self.date) +' | '+str(self.start_time)+' - '+str(self.end_time)
