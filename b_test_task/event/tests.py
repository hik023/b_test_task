from datetime import datetime, timedelta

from django.test import TestCase
from django.contrib.auth.models import User
from model_mommy import mommy

from event.models import Event, EventRegistration
from event.utils.event_helpers import (
    get_active_events,
    get_event_by_id,
    get_is_user_on_event,
)

class EventUtilsTestCase(TestCase):
    def setUp(self):
        self.u = mommy.make(User)
        self.e = mommy.make(Event, start_dt=datetime.now() + timedelta(days=3),
            _quantity=3)
        self.e_count = 3  # All events active


    def test_get_active_events(self):
        '''Test for correct active events calculation with new event'''
        mommy.make(Event, start_dt=datetime.now() + timedelta(days=3))
        active_e_qs = Event.objects.filter(start_dt__gte=datetime.now())
        test_e_qs = get_active_events()
        self.assertEqual(test_e_qs.count(), active_e_qs.count())

    
    def test_get_active_events_with_past(self):
        '''Test for correct active events calculation with event in past'''
        mommy.make(Event, start_dt=datetime.now() - timedelta(days=3))
        active_e_qs = Event.objects.filter(start_dt__gte=datetime.now())
        test_e_qs = get_active_events()
        self.assertEqual(test_e_qs.count(), active_e_qs.count())


    def test_get_event_by_id(self):
        '''Test for correct return event by id'''
        test_e = get_event_by_id(self.e[0].id)
        self.assertEqual(test_e, self.e[0])


    def test_get_is_user_on_event(self):
        '''Test for user event registration'''
        mommy.make(EventRegistration, user=self.u, event=self.e[0])
        self.assertTrue(get_is_user_on_event(self.e[0].id, self.u.id))
        self.assertFalse(get_is_user_on_event(self.e[1].id, self.u.id))