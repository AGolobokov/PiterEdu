from django.shortcuts import render, get_object_or_404

from community.models import Community
from community.forms import CommunityForm

from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def community(request):
    object_community = Community.objects.filter(is_active=True)
    form_community = CommunityForm(request.POST or None, initial={
        "object_room": object_community
    })
    if request.method == 'POST' and form_community.is_valid():
        form_community.save()
        return HttpResponseRedirect(reverse('community', kwargs={}))
    return render(request, 'communities.html', {'variable_community': object_community,
                                                'form_community': form_community
                                                })


def community_detail(request, community_id):
    name_community = get_object_or_404(Community, id=community_id)
    object_community = Community.objects.filter(is_active=True)
    return render(request, 'community_detail.html',
                  {'variable_community': object_community,
                   'name_community': name_community})
