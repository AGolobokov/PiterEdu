from django.shortcuts import render, get_object_or_404

from community.models import Community

# Create your views here.


def community(request):
    object_community = Community.objects.filter(is_active=True)
    return render(request, 'communities.html', {'variable_community': object_community})


def community_detail(request, community_id):
    name_community = get_object_or_404(Community, id=community_id)
    object_community = Community.objects.filter(is_active=True)
    return render(request, 'community_detail.html',
                  {'variable_community': object_community,
                   'name_community': name_community})
