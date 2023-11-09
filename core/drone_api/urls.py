from rest_framework import routers
from .api import MedicationViewSet, DroneViewSet


router = routers.DefaultRouter()
router.register('api/medication', MedicationViewSet, basename='medication')
router.register('api/drone', DroneViewSet, basename='drone')

urlpatterns = router.urls
