from django.test import TestCase
from drone_api.models import DroneModel, MedicationModel, ModelEnum, StateEnum

# Create your tests here.
class DroneTestCase(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.drone = DroneModel.objects.create(
            serial_number = '12345',
            model = ModelEnum.LIGHT,
            weight_limit = 500,
            battery_capacity = 100,
            state = StateEnum.IDLE
        )
        self.medication = MedicationModel.objects.create(
            name = 'abc-123_AAA',
            weight = 200,
            code = 'ABC_0099',
            image = None,
            drone = self.drone
        )
    
    def test_create_drone(self):
        self.assertEqual(DroneModel.objects.count(), 1)
        self.assertEqual(self.drone.serial_number, '12345')
        self.assertEqual(self.drone.model, 'Lightweight')
        self.assertEqual(self.drone.weight_limit, 500)
        self.assertEqual(self.drone.battery_capacity, 100)
        self.assertEqual(self.drone.state, 'IDLE')
    
    def test_create_medication(self):
        self.assertEqual(MedicationModel.objects.count(), 1)
        self.assertEqual(self.medication.name, 'abc-123_AAA')
        self.assertEqual(self.medication.weight, 200)
        self.assertEqual(self.medication.code, 'ABC_0099')
        self.assertEqual(self.medication.image, None)
        self.assertEqual(self.medication.drone.serial_number, '12345')
    
    def test_update_drone(self):
        self.drone.weight_limit = 300
        self.drone.battery_capacity = 20

        self.assertEqual(self.drone.weight_limit, 300)
        self.assertEqual(self.drone.battery_capacity, 20)

    def test_update_medication(self):
        self.medication.weight = 300
        self.medication.code = 'ABC_0099'

        self.assertEqual(self.medication.weight, 300)
        self.assertEqual(self.medication.code, 'ABC_0099')

    def test_delete_drone(self):
        self.drone.delete()
        self.assertEqual(DroneModel.objects.count(), 0)

    def test_delete_medication(self):
        self.medication.delete()
        self.assertEqual(MedicationModel.objects.count(), 0)
