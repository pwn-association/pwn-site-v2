# -*- coding: utf-8 -*-
""" PWN Event: event view """
from datetime import timedelta

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils.timezone import now

from ..models.event import Event
from ..models.season import Season
from ..app_settings import PAGINATION


class EventListView(ListView):
    """ """
    model = Event
    context_object_name = "event_list"


class EventBySeasonListView(ListView):
    """ """
    template_name = 'pwn_event/event_season_list.html'
    context_object_name = "events"

    def __init__(self):
        self.season = None

    def get_queryset(self, **kwargs):
        try:
            self.season = Season.objects.get(start_date__lte=now(), end_date__gte=now())
        except Season.DoesNotExist:
            self.season = None
        last_event_time = now().replace(hour=00, minute=00, second=00)
        if self.request.user.is_superuser:
            return Event.objects.filter(season=self.season, date__gte=last_event_time)
        return Event.published.filter(season=self.season, date__gte=last_event_time)

    def get_context_data(self, **kwargs):
        context = super(EventBySeasonListView, self).get_context_data(**kwargs)
        context['actual_season'] = self.season
        try:
            context["futur_season"] = Season.objects.get(
                start_date__year=now().year, start_date__month=9
            )
            context["futur_events"] = Event.objects.filter(
                date__year=now().year, date__month__gte=9
            )
        except Season.DoesNotExist:
            context["futur_season"] = None
            context["futur_events"] = None

        try:
            past_seasons = Season.objects.filter(start_date__lte=now())
        except Season.DoesNotExist:
            past_seasons = None

        context['past_seasons'] = past_seasons
        return context


class EventDetailView(DetailView):
    """ """
    model = Event
    context_object_name = "event"
    paginate_by = PAGINATION

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_superuser:
            return Event.objects.filter()
        return Event.published.filter()
