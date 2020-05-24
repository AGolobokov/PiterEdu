from django.shortcuts import render, get_object_or_404

from event.models import Event

# Create your views here.


def event(request):
    object_event = Event.objects.filter(is_active=True)
    #return render(request, 'events.html', locals())
    return render(request, 'events.html', {'variable_event': object_event})


def event_detail(request, event_id):
    name_event = get_object_or_404(Event, id=event_id)
    object_event = Event.objects.filter(is_active=True)
    return render(request, 'event_detail.html',
                  {'variable_event': object_event,
                   'name_event': name_event})

