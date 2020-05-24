from django.shortcuts import render
from project.models import Project, ProjectImage

# Create your views here.


def project(request):
    object_project = Project.objects.filter(is_active=True)
    object_image = ProjectImage.objects.filter(project__name__isnull=False)
    return render(request, 'projects.html', {'variable_project': object_project, 'variable_image': object_image})



