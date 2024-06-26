# -*- coding: utf-8 -*-
""" PWN Event: speaker view """

from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404

from ..models.speaker import Speaker
from ..models.event import Event
from ..app_settings import PAGINATION


class SpeakerListView(ListView):
    """ """
    model = Speaker
    context_object_name = "speaker_list"


class SpeakerDetailView(ListView):
    """ """
    template_name = 'pwn_event/speaker_detail.html'
    context_object_name = "event_list"
    paginate_by = PAGINATION

    def get_queryset(self, **kwargs):
        self.speaker = get_object_or_404(Speaker, slug=self.kwargs['slug'])
        return Event.published.filter(speakers=self.speaker)

    def get_context_data(self, **kwargs):
        context = super(SpeakerDetailView, self).get_context_data(**kwargs)
        context['speaker'] = self.speaker
        return context
