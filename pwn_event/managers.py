# -*- coding: utf-8 -*-
""" Creation: Managers """

from django.db import models
from django.utils import timezone


def event_published(queryset):
    """
    Return only the events published.
    """
    now = timezone.now()
    return queryset.filter(
        models.Q(start_publication__lte=now) |
        models.Q(start_publication=None),
        models.Q(end_publication__gt=now) |
        models.Q(end_publication=None),
        is_publish=True)


class EventPublishedManager(models.Manager):
    """
    Manager to retrieve published events.
    """

    def get_queryset(self):
        """
        Return published creations.
        """
        return event_published(
            super(EventPublishedManager, self).get_queryset())
