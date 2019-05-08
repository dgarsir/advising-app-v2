from django.db import models
from django.utils import timezone

class Appointment(models.Model):
	date=models.DateField(default=timezone.localdate)
	start_time=models.TimeField(default=timezone.now)
	end_time=models.TimeField(default=timezone.now)
	owner_EMPLID=models.CharField(default='',max_length=8)
	owner_name=models.CharField(default='', max_length=100)

	def _str_(self):
		return str(self.date) +' | '+str(self.start_time)+' - '+str(self.end_time)
