from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db.models.functions import Now
from django.db import models

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
#
# from .models.event import EventDate
# from .models.creation import Creation
# from .models.creation import PUBLISHED
# from .models.plugins import LatestEvents, EventsChoice, EventsMultiChoice
# from .utils import get_organized_events_by_date
#
# @plugin_pool.register_plugin
# class LatestEventsPlugin(CMSPluginBase):
#     """"todo: to remove"""
#     module = _('Creation')
#     name = _('Upcoming tour date')
#     model = LatestEvents
#     render_template = "creation/plugins/latest_events.html"
#     cache = False
#
#
# @plugin_pool.register_plugin
# class UpcomingTourDatesPlugin(CMSPluginBase):
#     module = _('Creation')
#     name = _('Upcoming tour date')
#     model = LatestEvents
#     render_template = "creation/plugins/latest_events.html"
#     cache = False
#
#     def render(self, context, instance, placeholder):
#         context = super(UpcomingTourDatesPlugin, self).render(context, instance, placeholder)
#
#         if instance.creation:
#             events = EventDate.published.filter(event__creation=instance.creation, date__gte=Now()).order_by('date')
#         else:
#             events = EventDate.published.filter(date__gte=Now()).order_by('date')
#
#         context['events'] = get_organized_events_by_date(events[:instance.events_number])
#         context['month_list'] = range(1, 13)
#
#         return context
#
#
# @plugin_pool.register_plugin
# class CreationDownloadFilesPlugin(CMSPluginBase):
#     module = _('Creation')
#     name = _('Download files')
#     model = EventsChoice
#     render_template = "creation/plugins/download_files.html"
#     cache = False
#
#     def render(self, context, instance, placeholder):
#         context = super(CreationDownloadFilesPlugin, self).render(context, instance, placeholder)
#         events = event = None
#
#         if instance.creation and instance.creation:
#             event = instance.creation
#         else:
#             events = Creation.published.all()
#
#         context['creations'] = events
#         context['creation'] = event
#         return context
#
#
# @plugin_pool.register_plugin
# class FeaturedCreationPlugin(CMSPluginBase):
#     module = _('Creation')
#     name = _('Featured creation')
#     model = EventsChoice
#     render_template = "creation/plugins/featured_event.html"
#     cache = False
#
#     def render(self, context, instance, placeholder):
#         context = super(FeaturedCreationPlugin, self).render(context, instance, placeholder)
#         context['event'] = None
#         try:
#             if instance.creation:
#                 context['event'] = Creation.published.get(id=instance.creation.id)
#         except Creation.DoesNotExist:
#             pass
#
#         return context
#
#
# @plugin_pool.register_plugin
# class MultiCreationsFeaturedPlugin(CMSPluginBase):
#     module = _('Creation')
#     name = _('Multi creation Featured')
#     model = EventsMultiChoice
#     render_template = "creation/plugins/multi_events_featured.html"
#     cache = False
#
#     def render(self, context, instance, placeholder):
#         now = timezone.now()
#         context = super(MultiCreationsFeaturedPlugin, self).render(context, instance, placeholder)
#         context['creations'] = instance.creations.filter(
#                                 models.Q(start_publication__lte=now) |
#                                 models.Q(start_publication=None),
#                                 models.Q(end_publication__gt=now) |
#                                 models.Q(end_publication=None),
#                                 status=PUBLISHED)
#
#         return context
