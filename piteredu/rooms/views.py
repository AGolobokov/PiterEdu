from django.shortcuts import render, get_object_or_404
from rooms.models import Rooms
from rooms.forms import RoomForm

from subscriber import forms
from subscriber.forms import SubscriberForm

from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def room(request):
    form_subscriber = forms.SubscriberForm(request.POST or None)
    if request.method == 'POST' and form_subscriber.is_valid():
        form_subscriber.save()
    object_room = Rooms.objects.filter(is_active=True)
    form_room = RoomForm(request.POST or None, request.FILES, initial={
        "object_room": object_room
    })
    if request.method == 'POST' and form_room.is_valid():
        form_room.save()
        #return HttpResponseRedirect(reverse('rooms', kwargs={}))
    return render(request, 'rooms.html', {'variable_room': object_room,
                                          'form_room': form_room,
                                          'form_subscriber': form_subscriber
                                          })


def room_detail(request, room_id):
    form_subscriber = forms.SubscriberForm(request.POST or None)
    if request.method == 'POST' and form_subscriber.is_valid():
        form_subscriber.save()
    name_room = get_object_or_404(Rooms, id=room_id)
    object_room = Rooms.objects.filter(is_active=True)

    return render(request, 'room_detail.html',
                  {'variable_room': object_room,
                   'name_room': name_room,
                   'form_subscriber': form_subscriber
                   })
