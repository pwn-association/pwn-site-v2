# -*- coding: utf-8 -*-
""" PWN Events: Template tags """

from django import template as dj_template
from django.db.models import Count

from ..models.tag import Tag
from ..models.event import Event

register = dj_template.Library()


@register.inclusion_tag('pwn_event/template_tags/dummy.html', takes_context=True)
def get_tags(context, template='pwn_event/template_tags/tags.html'):
    """
    Return the published categories.
    """
    return {'template': template,
            'tags': Tag.objects.all(),
            # 'tags': Tag.published.all().annotate(count_creations_published=Count('events')),
            'context_tag': context.get('tag')}


@register.inclusion_tag('pwn_event/template_tags/dummy.html')
def get_last_events(number=5, template='pwn_event/template_tags/last_events.html'):
    """
    Return the most recent creations.
    """
    return {'template': template,
            'events': Event.objects.all()[:number]}
            # 'events': Event.published.all()[:number]}
