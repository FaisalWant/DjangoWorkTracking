from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


hours=([(str(x), str(x)) for x in range(1,25)])

class Report(models.Model):
	day=models.DateField(default=timezone.now)
	start_hour=models.CharField(max_length=2, choices=hours)
	end_hour=models.CharField(max_length=2, choices=hours)
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	# product=
	plan=models.PositiveIntegerField()
	execution=models.PositiveIntegerField()
	# production_line=
	updated=models.DateTimeField(auto_now=True)
	created=models.DateTimeField(auto_now_add=True)
