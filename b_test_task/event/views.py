from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.http.request import HttpRequest
from django.http.response import HttpResponse

from event.utils.event_helpers import (
    get_active_events,
    get_event_by_id,
    get_is_user_on_event,
)
from event.forms import EventRegistrationForm


def main_page(request: HttpRequest) -> HttpResponse:
    print(request)
    if request.user.is_authenticated:
        return render(request, 'event/home_page.html', context={})
    else: 
        return redirect('login')


@login_required
def event_list(request: HttpRequest) -> HttpResponse:
    data = {}
    events = get_active_events()
    data['events'] = events
    return render(request, 'event/event_list.html', context=data)


@login_required
def event_detail(request: HttpRequest, event_id: int) -> HttpResponse:
    data = {}
    data['event'] = get_event_by_id(event_id)
    data['on_event'] = get_is_user_on_event(event_id, request.user.id)
    return render(request, 'event/event_detail.html', context=data)


@login_required
@require_http_methods(["POST"])
def register_on_event(request: HttpRequest) -> HttpResponse:
    if get_is_user_on_event(
        request.POST.get('event'), request.POST.get('user')
        ):
        redirect(
            'event:event_detail', 
            event_id=request.POST.get('event')
            )

    form = EventRegistrationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(
            'event:event_detail', 
            event_id=request.POST.get('event')
            )
