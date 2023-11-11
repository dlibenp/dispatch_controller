from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
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
    weight_limit = models.DecimalField(null=True, max_digits=5, decimal_places=2, validators=[MinValueValidator(0.0), MaxValueValidator(500.00)])
    battery_capacity = models.IntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(100)])
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
    name = models.CharField(max_length=255, null=True, validators=[RegexValidator(r'^[a-zA-Z0-9-_]+$')])
    weight = models.DecimalField(null=True, max_digits=5, decimal_places=2, validators=[MinValueValidator(0.0), MaxValueValidator(500.00)])
    code = models.CharField(max_length=255, null=True, validators=[RegexValidator(r'^[A-Z0-9_]+$')])
    image = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True, null=True)
    drone = models.ForeignKey(DroneModel, on_delete=models.CASCADE, null=True, blank=True, related_name='medications')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'MedicationModel'
        verbose_name_plural = 'MedicationModels'
        ordering = ['-created_at']

    def __str__(self):
        return self.name