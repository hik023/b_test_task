from django.contrib.auth.models import User
from django.db.models import QuerySet

from rest_framework import serializers

from event.models import (
    Event,
    EventRegistration
)


class EventListSerializer(serializers.HyperlinkedModelSerializer):
    is_somebody_register = serializers.SerializerMethodField()
    link = serializers.SerializerMethodField()
    started_at = serializers.CharField(source='start_dt')

    def get_is_somebody_register(self, obj: Event) -> bool:
        '''Returns True if somebody registered on event'''
        return EventRegistration.objects.filter(event=obj).exists()

    def get_link(self, obj: Event) -> str:
        '''\
        Imitate HyperlinkedRelatedField, because no idea why it not works here 
        \n :(

        '''
        return f'{self.context["request"].build_absolute_uri()}{obj.id}'

    class Meta:
        model = Event
        fields = [
            'id','title', 'description', 
            'started_at', 'link', 'link','is_somebody_register'
            ]


class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='first_name')
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'name']



class EventDetailSerializer(serializers.ModelSerializer):
    participants = serializers.SerializerMethodField()
    started_at = serializers.CharField(source='start_dt')

    def get_participants(self, obj: Event) -> dict:
        '''Returns participants on event'''
        users_list = EventRegistration.objects.filter(
            event=obj).values_list('user', flat=True)
        users = User.objects.filter(pk__in=users_list)
        serialized = UserSerializer(users, many=True)
        return serialized.data

    class Meta:
        model = Event
        fields = ['title', 'description', 'started_at', 'participants']


class EventRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventRegistration
        fields = ['event', 'user']