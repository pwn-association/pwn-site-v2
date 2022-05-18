# -*- coding: utf-8 -*-
""" Creation: Defaults urls """

from django.urls import include, path
from django.views.generic import TemplateView

from .views.place import PlaceListView, PlaceDetailView
from .views.speaker import SpeakerListView, SpeakerDetailView
from .views.season import SeasonListView, SeasonDetailView
from .views.tag import TagDetailView, TagListView
from .views.event import EventListView, EventDetailView, EventBySeasonListView

app_name = 'pwn_event'

urlpatterns = [
    # Places
    path('places/', PlaceListView.as_view(), name='place_list'),
    path('places/<slug:slug>/', PlaceDetailView.as_view(), name='place_detail'),

    # Speakers
    path('speakers/', SpeakerListView.as_view(), name='speaker_list'),
    path('speakers/<slug:slug>/', SpeakerDetailView.as_view(), name='speaker_detail'),

    # Season
    path(r'seasons/', SeasonListView.as_view(), name='season_list'),
    path(r'seasons/<slug:slug>/', SeasonDetailView.as_view(), name='season_detail'),

    # TAg
    path(r'tags/', TagListView.as_view(), name='tag_list'),
    path(r'tags/<slug:slug>/', TagDetailView.as_view(), name='tag_detail'),

    # Events
    path('events/', EventListView.as_view(), name='event_list'),
    path('events/seasons/', EventBySeasonListView.as_view(), name='event_season_list'),
    path('events/<slug:slug>', EventDetailView.as_view(), name='event_detail'),

    # # Home
    path('', TemplateView.as_view(template_name='pwn_event/home.html'), name='event_home'),
]

