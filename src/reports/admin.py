from django.contrib import admin

# Register your models here.
from .models import Report, ProblemReported

admin.site.register(ProblemReported)
admin.site.register(Report) 