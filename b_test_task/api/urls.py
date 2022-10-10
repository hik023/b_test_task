from rest_framework import routers

from api.views import EventViewSet, EventRegistrationViewSet


router = routers.DefaultRouter()
router.register(r'events', EventViewSet, 'event-api')
router.register(r'event_register', EventRegistrationViewSet, 
                    'event_register')

urlpatterns = router.urls