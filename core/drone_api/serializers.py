from rest_framework import serializers
from .models import MedicationModel, DroneModel


class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationModel
        fields = ('id', 'name', 'weight', 'code', 'image', 'drone', 'created_at')
        read_only_fields = ('created_at',)
    
    def validate(self, attrs):
        drone_data = attrs.get('drone')
        total_weight = sum(data.weight for data in drone_data.medications.all())

        if (total_weight + attrs.get('weight')) > drone_data.weight_limit:
            raise serializers.ValidationError("Total weight of medications exceeds weight limit of the drone.")
        
        return super().validate(attrs)


class DroneSerializer(serializers.ModelSerializer):
    medications = MedicationSerializer(many=True, read_only=True)
    class Meta:
        model = DroneModel
        fields = ('id', 'serial_number', 'model', 'weight_limit', 'battery_capacity', 'state', 'medications', 'created_at')
        read_only_fields = ('created_at',)
    
    def validate(self, attrs):
        data_battery = attrs.get('battery_capacity')
        data_state = attrs.get('state')
        if data_battery < 25 and data_state == 'LOADING':
            raise serializers.ValidationError("State cannot be LOADING if the battery level is below 25%.")
        return super().validate(attrs)
