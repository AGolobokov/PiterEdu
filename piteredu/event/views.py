from django.shortcuts import render, get_object_or_404

from event.models import Event
from event.forms import EventForm

from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def event(request):
    object_event = Event.objects.filter(is_active=True)
    form_event = EventForm(request.POST or None, initial={
        "object_event": object_event
    })
    if request.method == 'POST' and form_event.is_valid():
        form_event.save()
        return HttpResponseRedirect(reverse('event', kwargs={}))
    #return render(request, 'events.html', locals())
    return render(request, 'events.html', {'variable_event': object_event,
                                           'form_event': form_event
                                           })


def event_detail(request, event_id):
    name_event = get_object_or_404(Event, id=event_id)
    object_event = Event.objects.filter(is_active=True)
    return render(request, 'event_detail.html',
                  {'variable_event': object_event,
                   'name_event': name_event})

