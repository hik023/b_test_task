from django.contrib import admin
from event.models import Event, EventRegistration


class EventRegistrationInline(admin.StackedInline):
    model = EventRegistration


class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'start_dt']
    ordering = ['start_dt']
    inlines = [EventRegistrationInline]


class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ['event', 'user']
    ordering = ['event']


admin.site.register(Event, EventAdmin)
admin.site.register(EventRegistration, EventRegistrationAdmin)