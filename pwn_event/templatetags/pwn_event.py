# -*- coding: utf-8 -*-
""" PWN Events: Template tags """

from django import template as dj_template
from django.utils.timezone import now

from ..models.tag import Tag
from ..models.event import Event
from ..models.season import Season


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

    season = Season.objects.get(start_date__lte=now(), end_date__gte=now())
    last_event_time = now().replace(hour=00, minute=00, second=00)
    events = Event.published.filter(season=season, date__gte=last_event_time)[:number]

    return {'template': template, 'events': events}

