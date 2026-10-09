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


@register.inclusion_tag('pwn_event/template_tags/dummy.html', takes_context=True)
def get_last_events(context, number=3, template='pwn_event/template_tags/last_events.html'):
    """
    Return the most recent creations.
    """

    try:
        season = Season.objects.get(start_date__lte=now(), end_date__gte=now())
    except Season.DoesNotExist:
        season = None
    last_event_time = now().replace(hour=00, minute=00, second=00)
    request = context['request']
    if request.user.is_superuser:
        events = Event.objects
    else:
        events = Event.published

    events = reversed(events
              .filter(season=season, date__gte=last_event_time)
              .order_by('date')[:number])

    return {'template': template, 'events': events}


@register.inclusion_tag('pwn_event/template_tags/dummy.html', takes_context=True)
def get_futur_season_events(context, number=3, template='pwn_event/template_tags/last_events.html'):
    """
    Return the most recent creations.
    """
    request = context["request"]

    current_season = Season.get_current()
    next_season = current_season.get_next() if current_season else None

    events = Event.published
    if request.user.is_superuser:
        events = Event.objects

    if next_season is None:
        events = Event.objects.none()
    else:
        events = reversed(events.filter(season=next_season).order_by('date')[:number])


    return {
        'template': template,
        'events': events,
    }


@register.simple_tag
def is_futur_season_exist():
    """
    Return True if the futur season exists.
    """
    current_season = Season.get_current()
    next_season = current_season.get_next() if current_season else None

    if next_season is None:
        return False

    return Event.published.filter(season=next_season).exists()

