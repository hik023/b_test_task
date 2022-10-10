from event.models import Event, EventRegistration
from django.db.models import QuerySet
from datetime import datetime


def get_active_events() -> QuerySet[Event]:
    '''
    Returns active events
    '''
    return Event.objects.filter(start_dt__gte=datetime.now())


def get_event_by_id(event_id: int) -> Event:
    '''
    Returns event by id
    '''
    return Event.objects.get(pk=event_id)


def get_is_user_on_event(event_id: int, user_id: int) -> bool:
    '''
    Returns if user registered on event or not
    '''
    er_record = EventRegistration.objects.filter(
        event__id=event_id, user__id=user_id
        )
    return er_record.exists()