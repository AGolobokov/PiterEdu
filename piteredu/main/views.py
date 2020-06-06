from django.shortcuts import render
from subscriber.models import Subscriber
from subscriber.forms import SubscriberForm

from subscriber import forms

from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def home(request):
    form_subscriber = forms.SubscriberForm(request.POST or None)
    if request.method == 'POST' and form_subscriber.is_valid():
        form_subscriber.save()
        return HttpResponseRedirect(reverse('home'))
    return render(request, 'home.html', {'form_subscriber': form_subscriber})


def about(request):
    return render(request, 'about.html', {})
