from django.shortcuts import render, get_object_or_404
from resource.models import Resource
# Create your views here.


def resource(request):
    object_resource = Resource.objects.filter(is_active=True)
    return render(request, 'resource.html', {'variable_resource':object_resource})


def resource_detail(request, resource_id):
    name_resource = get_object_or_404(Resource, id=resource_id)
    object_resource = Resource.objects.filter(is_active=True)
    return render(request, 'resource_detail.html',
                  {'variable_resource': object_resource,
                   'name_resource': name_resource})
