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

    def _get_events_by_user_type_qs(self):
        """Retourne les événements publiés ou non selon si l'utilisateur est admin ou pas"""
        events = Event.published
        if self.request.user.is_superuser:
            events = Event.objects
        return events.filter()

    def get_queryset(self, **kwargs):
        """Retourne les prochains events de la saison en cours."""
        events = self._get_events_by_user_type_qs()
        return events.filter(
            season=Season.get_current(),
            date__gte=now().date(),
        )


    def get_context_data(self, **kwargs):
        """Retourne dans le contexte, les evenements de la prochaine saison et des saisons passées"""
        context = super(EventBySeasonListView, self).get_context_data(**kwargs)

        current_season = Season.get_current()
        next_season = current_season.get_next() if current_season else None
        events = self._get_events_by_user_type_qs()

        context.update({
            "futur_season": next_season,
            "futur_events": events.filter(season=next_season),
            "past_seasons": Season.objects.filter(start_date__lte=now()).order_by('start_date'),
        })

        return context


class EventDetailView(DetailView):
    """ """
    model = Event
    context_object_name = "event"
    paginate_by = PAGINATION

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_superuser:
            return Event.objects
        return Event.published
