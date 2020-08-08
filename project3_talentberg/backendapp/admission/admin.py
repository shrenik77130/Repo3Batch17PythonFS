from django.contrib import admin
from .models import Admission,AdmissionStatus

# Register your models here.
admin.site.register(Admission)
admin.site.register(AdmissionStatus)
