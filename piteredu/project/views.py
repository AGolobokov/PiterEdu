from django.shortcuts import render
from project.models import Project, ProjectImage

from subscriber import forms
from subscriber.forms import SubscriberForm

# Create your views here.


def project(request):
    form_subscriber = forms.SubscriberForm(request.POST or None)
    if request.method == 'POST' and form_subscriber.is_valid():
        form_subscriber.save()
    object_project = Project.objects.filter(is_active=True)
    object_image = ProjectImage.objects.filter(project__name__isnull=False)
    return render(request, 'projects.html', {'variable_project': object_project,
                                             'variable_image': object_image,
                                             'form_subscriber': form_subscriber
                                             })



