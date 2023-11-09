from rest_framework import serializers
from .models import MedicationModel, DroneModel


class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationModel
        fields = ('id', 'name', 'weight', 'code', 'image', 'drone', 'created_at')
        read_only_fields = ('created_at',)


class DroneSerializer(serializers.ModelSerializer):
    class Meta:
        model = DroneModel
        fields = ('id', 'serial_number', 'model', 'weight', 'battery_capacity', 'state', 'created_at')
        read_only_fields = ('created_at',)
