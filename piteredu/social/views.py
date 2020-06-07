from django.shortcuts import render

from subscriber import forms
from subscriber.forms import SubscriberForm

# Create your views here.


def social(request):
    form_subscriber = forms.SubscriberForm(request.POST or None)
    if request.method == 'POST' and form_subscriber.is_valid():
        form_subscriber.save()
    return render(request, 'social.html', {'form_subscriber': form_subscriber})
