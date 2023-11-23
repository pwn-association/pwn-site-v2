# -*- coding: utf-8 -*-
""" PWN Event: place view """

from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404

from ..models.place import Place
from ..models.event import Event
from ..app_settings import PAGINATION


class PlaceListView(ListView):
    """ """
    model = Place
    context_object_name = "place_list"


class PlaceDetailView(ListView):
    """ """
    template_name = 'pwn_event/place_detail.html'
    context_object_name = "event_list"
    paginate_by = PAGINATION

    def get_queryset(self, **kwargs):
        self.place = get_object_or_404(Place, slug=self.kwargs['slug'])
        return Event.objects.filter(place=self.place)
        # return Event.published.filter(categories=self.category)

    def get_context_data(self, **kwargs):
        context = super(PlaceDetailView, self).get_context_data(**kwargs)
        context['place'] = self.place
        return context
