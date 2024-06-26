# -*- coding: utf-8 -*-
""" PWN Event: season view """

from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404

from ..models.season import Season
from ..models.event import Event
from ..app_settings import PAGINATION


class SeasonListView(ListView):
    """ """
    model = Season
    context_object_name = "season_list"


class SeasonDetailView(ListView):
    """ """
    template_name = 'pwn_event/season_detail.html'
    context_object_name = "event_list"
    paginate_by = PAGINATION

    def get_queryset(self, **kwargs):
        self.season = get_object_or_404(Season, slug=self.kwargs['slug'])
        return Event.published.filter(season=self.season)

    def get_context_data(self, **kwargs):
        context = super(SeasonDetailView, self).get_context_data(**kwargs)
        context['season'] = self.season
        return context
