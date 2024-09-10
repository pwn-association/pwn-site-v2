# -*- coding: utf-8 -*-
from time import mktime
from datetime import datetime, timedelta

from django.http import JsonResponse
from django.utils.html import strip_tags

from ..models import Event


def n8n_json_view(request):
    from django.utils import timezone
    domain = 'https://pwn-association.org'
    now = timezone.now()

    data = {}

    event = Event.published.filter(date__gte=now, n8n=True).order_by('-date').last()

    if event:
        timestamp = get_timestamp(event.date)
        authors = get_authors(event)
        description = event.description.replace("\n", "")
        image = None
        if event.image:
            image = domain + event.image.url

        data = {
            "dataStart": timestamp,
            "title": event.title,
            "author": authors,
            "image": image,
            "url": domain + event.get_absolute_url(),
            "description": strip_tags(description)
        }

    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def get_timestamp(date):
    date = date + timedelta(hours=2)
    element = datetime.strptime(str(date), '%Y-%m-%d %H:%M:%S%z')
    tuple = element.timetuple()
    timestamp = mktime(tuple)

    return timestamp


def get_authors(event):
    speakers = ''
    for speaker in event.speakers.all():
        speakers += f"{speaker}, "
    if speakers != '':
        speakers = speakers[:-2]
    return speakers
