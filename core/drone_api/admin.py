from django.contrib import admin
from .models import MedicationModel, DroneModel

# Register your models here.
admin.site.register(MedicationModel)
admin.site.register(DroneModel)
