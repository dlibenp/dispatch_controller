from django.db import models
import uuid


# Create your models here.
class ModelEnum(models.TextChoices):
    LIGHT = 'Lightweight'
    MIDDLE = 'Middleweight'
    CRUISER = 'Cruiserweight'
    HEAVY = 'Heavyweight'


class StateEnum(models.TextChoices):
    IDLE = 'IDLE'
    LOADING = 'LOADING'
    LOADED = 'LOADED'
    DELIVERING = 'DELIVERING'
    DELIVERED = 'DELIVERED'
    RETURNING = 'RETURNING'


class DroneModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    serial_number = models.CharField(max_length=100, null=True)
    model = models.CharField(max_length=20, choices=ModelEnum.choices, default=ModelEnum.LIGHT,)
    weight = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    battery_capacity = models.IntegerField(null=True)
    state = models.CharField(max_length=20, choices=StateEnum.choices, default=StateEnum.IDLE,)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'DroneModel'
        verbose_name_plural = 'DroneModels'
        ordering = ['-created_at']

    def __str__(self):
        return self.serial_number


class MedicationModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255, null=True)
    weight = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    code = models.CharField(max_length=255, null=True)
    image = models.CharField(max_length=255, null=True)
    drone = models.ForeignKey(DroneModel, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'MedicationModel'
        verbose_name_plural = 'MedicationModels'
        ordering = ['-created_at']

    def __str__(self):
        return self.name