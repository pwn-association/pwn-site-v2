# -*- coding: utf-8 -*-
""" Event model for Creation """
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField


EVENT_START_SEASON_MONTH = 9
EVENT_END_SEASON_MONTH = 8


class Season(models.Model):
    """ """
    name = models.CharField(_('name'), max_length=250, unique=True)
    slug = AutoSlugField(_('slug'), max_length=255, populate_from=['name'], unique=True, db_index=True)
    start_date = models.DateField(_('start date'),)
    end_date = models.DateField(_('end date'),)

    class Meta:
        get_latest_by = '-start_date'
        verbose_name = _('Season')
        verbose_name_plural = _('Seasons')
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Builds and returns the category's URL
        based on his tree path.
        """
        return reverse('pwn_event:season_detail', kwargs={'slug': self.slug})

    @classmethod
    def get_current(cls):
        """Return current season"""
        today = timezone.now().date()
        return cls.objects.filter(
            start_date__lte=today,
            end_date__gte=today,
        ).first()

    def get_next(self):
        """Return the next season"""
        return self.__class__.objects.filter(
            start_date__gt=self.end_date,
        ).order_by('start_date').first()


    def is_current(self):
        """Return True if the season is the current season, False else"""
        today = timezone.now().date()
        return self.start_date <= today <= self.end_date


