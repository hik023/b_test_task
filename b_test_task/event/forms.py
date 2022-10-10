from django.forms import ModelForm
from event.models import EventRegistration


class EventRegistrationForm(ModelForm):
    class Meta:
        model = EventRegistration
        fields = ['event', 'user']