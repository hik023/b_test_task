from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework import permissions
from rest_framework.request import Request

from event.models import Event
from .serializers import (
    EventListSerializer, 
    EventDetailSerializer,
    EventRegistrationSerializer
)


class EventViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def list(self, request: Request) -> Response:
        queryset = Event.objects.all()
        serializer = EventListSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request: Request, pk: int=None) -> Response:
        queryset = Event.objects.all()
        event = get_object_or_404(queryset, id=pk)
        serializer = EventDetailSerializer(event)
        return Response(serializer.data)


class EventRegistrationViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [SessionAuthentication]

    def create(self, request: Request, *args, **kwargs) -> Response:
        data = {
            'event': request.data['event'],
            'user': request.user.id
        }
        serializer = EventRegistrationSerializer(data=data)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

   