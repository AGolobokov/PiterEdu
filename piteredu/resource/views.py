from django.shortcuts import render, get_object_or_404
from resource.models import Resource
from resource.forms import ResourceForm

from subscriber import forms
from subscriber.forms import SubscriberForm

from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.


def resource(request):
    form_subscriber = forms.SubscriberForm(request.POST or None)
    if request.method == 'POST' and form_subscriber.is_valid():
        form_subscriber.save()
    object_resource = Resource.objects.filter(is_active=True)
    form_resource = ResourceForm(request.POST or None, request.FILES, initial={
        "object_resource": object_resource
    })
    if request.method == 'POST' and form_resource.is_valid():
        form_resource.save()
        #return HttpResponseRedirect(reverse('resource', kwargs={}))
    return render(request, 'resource.html', {'variable_resource': object_resource,
                                             'form_resource': form_resource,
                                             'form_subscriber': form_subscriber
                                             })


def resource_detail(request, resource_id):
    form_subscriber = forms.SubscriberForm(request.POST or None)
    if request.method == 'POST' and form_subscriber.is_valid():
        form_subscriber.save()
    name_resource = get_object_or_404(Resource, id=resource_id)
    object_resource = Resource.objects.filter(is_active=True)
    return render(request, 'resource_detail.html',
                  {'variable_resource': object_resource,
                   'name_resource': name_resource,
                   'form_subscriber': form_subscriber
                   })
