from django.shortcuts import render, get_object_or_404

from event.models import Event
from event.forms import EventForm

from subscriber.forms import SubscriberForm
from subscriber import forms

from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def event(request):
    form_subscriber = forms.SubscriberForm(request.POST or None)
    if request.method == 'POST' and form_subscriber.is_valid():
        form_subscriber.save()
    object_event = Event.objects.filter(is_active=True)
    form_event = EventForm(request.POST or None,request.FILES, initial={
        "object_event": object_event
    })
    if request.method == 'POST' and form_event.is_valid():
        form_event.save()
        return HttpResponseRedirect(reverse('event', kwargs={}))
    #return render(request, 'events.html', locals())
    return render(request, 'events.html', {'variable_event': object_event,
                                           'form_event': form_event,
                                           'form_subscriber': form_subscriber
                                           })


def event_detail(request, event_id):
    form_subscriber = forms.SubscriberForm(request.POST or None)
    if request.method == 'POST' and form_subscriber.is_valid():
        form_subscriber.save()
    name_event = get_object_or_404(Event, id=event_id)
    object_event = Event.objects.filter(is_active=True)
    return render(request, 'event_detail.html',
                  {'variable_event': object_event,
                   'name_event': name_event,
                   'form_subscriber': form_subscriber
                   })

