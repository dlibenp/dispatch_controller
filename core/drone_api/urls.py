from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from .api import MedicationViewSet, DroneViewSet


router = routers.DefaultRouter()
router.register('api/medication', MedicationViewSet, basename='medication')
router.register('api/drone', DroneViewSet, basename='drone')

urlpatterns = router.urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)