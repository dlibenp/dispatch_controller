from rest_framework import viewsets, permissions
from django.core.cache import cache
import logging
from .models import MedicationModel, DroneModel
from .serializers import MedicationSerializer, DroneSerializer


class MedicationViewSet(viewsets.ModelViewSet):
    serializer_class = MedicationSerializer
    queryset = MedicationModel.objects.all()
    permission_classes = [permissions.AllowAny]


class DroneViewSet(viewsets.ModelViewSet):
    serializer_class = DroneSerializer
    queryset = DroneModel.objects.all()
    permission_classes = [permissions.AllowAny]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            drone_data = cache.get('drone')
            if drone_data:
                self.initialize_api(data=drone_data)
            else:
                data = {
                    'serial_number': '12345',
                    'model': 'LIGHT',
                    'weight_limit': 500,
                    'battery_capacity': 100,
                    'state': 'IDLE'
                }
                cache.set('drone', data)
                self.initialize_api(data=data)
        except Exception as ex:
            logging.error(msg=f'ERROR: {ex}')

    def initialize_api(self, data):
        drone = DroneModel.objects.create(
            serial_number = data['serial_number'],
            model = data['model'],
            weight_limit = data['weight_limit'],
            battery_capacity = data['battery_capacity'],
            state = data['state']
        )
        drone.save()