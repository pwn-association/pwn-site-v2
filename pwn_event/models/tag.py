# -*- coding: utf-8 -*-
""" Tag model for PWN Event """

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from django_extensions.db.fields import AutoSlugField


class Tag(models.Model):
    """
    """

    name = models.CharField(_('name'), max_length=255)
    slug = AutoSlugField(_('slug'), unique=True, max_length=255, db_index=True, populate_from=['name'],
                         help_text=_("Used to build the tag's URL."))
    description = models.TextField(_('description'), blank=True)

    class Meta:
        """
        Tag's meta information.
        """
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Builds and returns the tag's URL
        based on his tree path.
        """
        return reverse('pwn_event:tag_detail', kwargs={'slug': self.slug})

    # def event_published(self):
    #     """
    #     Returns tag's published creations.
    #     """
    #     return tag_published(self.events)



