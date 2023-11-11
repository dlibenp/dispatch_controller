import pytest
from rest_framework import status
from rest_framework.test import APIClient
from drone_api.models import DroneModel, ModelEnum, StateEnum


@pytest.mark.django_db
def test_create_drone():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    data = {
        'serial_number': '12345',
        'model': ModelEnum.LIGHT,
        'weight_limit': 500,
        'battery_capacity': 100,
        'state': StateEnum.IDLE,
    }

    client = APIClient()
    response = client.post('/api/drone/', data, format='json', **headers)

    assert response.status_code == status.HTTP_201_CREATED
    assert DroneModel.objects.count() == 1