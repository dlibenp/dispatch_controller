from rest_framework import viewsets, permissions
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