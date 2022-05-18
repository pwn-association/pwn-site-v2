# -*- coding: utf-8 -*-
""" PWN Event: tag view """

from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404

from ..models.tag import Tag
from ..models.event import Event
from ..app_settings import PAGINATION


class TagListView(ListView):
    """ """
    model = Tag
    context_object_name = "tag_list"


class TagDetailView(ListView):
    """ """
    template_name = 'pwn_event/tag_detail.html'
    context_object_name = "event_list"
    paginate_by = PAGINATION

    def get_queryset(self, **kwargs):
        self.tag = get_object_or_404(Tag, slug=self.kwargs['slug'])
        return Event.objects.filter(tags=self.tag)
        # return Event.published.filter(categories=self.category)

    def get_context_data(self, **kwargs):
        context = super(TagDetailView, self).get_context_data(**kwargs)
        context['tag'] = self.tag
        return context
