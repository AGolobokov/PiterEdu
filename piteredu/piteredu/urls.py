"""piteredu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from django.conf.urls.static import static
from django.conf import settings

from main import views as homeviews
from event import views as eventviews
from community import views as communityviews
from social import views as socialviews
from rooms import views as roomsviews
from resource import views as resourceviews
from project import views as projectviews
from subscriber import views as subscriberviews



urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', homeviews.home, name='home'),
    #url(r'^new$', homeviews.subscriber, name='subscriber'),
    url(r'^about$', homeviews.about, name='about'),
    url(r'^events$', eventviews.event, name='event'),
    url(r'^communities$', communityviews.community, name='community'),
    url(r'^social$', socialviews.social, name='social'),
    url(r'^rooms$', roomsviews.room, name='rooms'),
    url(r'^resource$', resourceviews.resource, name='resource'),
    url(r'^projects$', projectviews.project, name='project'),
    url(r'^events/(?P<event_id>\d+)$', eventviews.event_detail, name='event-detail'),
    url(r'^communities/(?P<community_id>\d+)$', communityviews.community_detail, name='community-detail'),
    url(r'^rooms/(?P<room_id>\d+)$', roomsviews.room_detail, name='room-detail'),
    url(r'^resource/(?P<resource_id>\d+)$', resourceviews.resource_detail, name='resource-detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
