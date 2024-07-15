from django.contrib import admin
from .models import Patient, Rdv, ordonnance

# Register your models here.

admin.site.register(Patient),
admin.site.register(Rdv),
admin.site.register(ordonnance)