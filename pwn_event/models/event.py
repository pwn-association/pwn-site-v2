# -*- coding: utf-8 -*-
""" Event model for Creation """

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.timezone import now

from django_extensions.db.fields import AutoSlugField
from filer.fields.image import FilerImageField
# from ckeditor.fields import RichTextField
from django_ckeditor_5.fields import CKEditor5Field as RichTextField

from ..models.place import Place
from ..models.speaker import Speaker
from ..models.season import Season
from ..models.tag import Tag
from ..managers import EventPublishedManager
from ..utils import get_or_create_season


class Event(models.Model):
    """ """
    title = models.CharField(_('title'), max_length=250)
    slug = AutoSlugField(_('slug'), max_length=255, populate_from=['title'], unique=True, db_index=True)
    image = FilerImageField(default=None, verbose_name=_("image"), null=True, blank=True, on_delete=models.SET_NULL)
    excerpt = RichTextField(_('excerpt'), blank=True, null=True)
    description = RichTextField(_('description'), blank=True, null=True)
    place = models.ForeignKey(Place, on_delete=models.SET_NULL, verbose_name=_('place'), related_name="events",
                              null=True, blank=True)
    speakers = models.ManyToManyField(Speaker, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    date = models.DateTimeField(_('Event date'))
    season = models.ForeignKey(Season, on_delete=models.PROTECT,
                               verbose_name=_('season'), related_name="events", null=True, blank=True)

    n8n = models.BooleanField(_('n8n'), default=True, help_text="La conférence est-elle visible par n8n ?")
    is_publish = models.BooleanField(_('is publish'), default=False)
    start_publication = models.DateTimeField(_('start publication'), blank=True, null=True,
                                             help_text=_('Start date of publication.'))
    end_publication = models.DateTimeField(_('end publication'), blank=True, null=True,
                                           help_text=_('End date of publication.'))

    objects = models.Manager()
    published = EventPublishedManager()

    class Meta:
        get_latest_by = '-date'
        verbose_name = _('Event')
        verbose_name_plural = _('Events')
        ordering = ('-date', )

    def __str__(self):
        return f"{self.date} : {self.title}"

    def get_absolute_url(self):
        """
        Builds and returns the category's URL
        based on his tree path.
        """
        return reverse('pwn_event:event_detail', kwargs={'slug': self.slug})

    def is_passed(self):
        """ Check if the event is passed """
        last_event_time = now().replace(hour=00, minute=00, second=00) # todo : utilisé à plusieurs endroitn faire une fonction
        if self.date <= last_event_time:
            return True
        return False

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        season = get_or_create_season(self.date)
        self.season = season

        super().save(force_insert, force_update, using, update_fields)