from django.urls import path
from event.views import (
     main_page, 
     event_list,
     event_detail,
     register_on_event,
)


urlpatterns = [
     path('', main_page, name='home'),
     path('event_list', event_list, name='event_list'),
     path('event/<int:event_id>', event_detail, name='event_detail'),
     path('event_register', register_on_event, name='event_register'),
]
