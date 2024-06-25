"""Toolbar extensions for CMS"""
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool


@toolbar_pool.register
class ConferenceToolbar(CMSToolbar):

    def populate(self):
        user = self.request.user
        conf_menu = self.toolbar.get_or_create_menu(
            'confs-menu', _('Conférences'))

        # Changelist
        url = reverse('admin:pwn_event_event_changelist')
        conf_menu.add_sideframe_item(
            _('Liste des conférences'), url=url,
            disabled=not user.has_perm('pwn_event.change_event'))

        # Add Conf
        url = reverse('admin:pwn_event_event_add')
        conf_menu.add_modal_item(
            _('Ajouter une conférences'), url=url,
            disabled=not user.has_perm('pwn_event.change_event'))

        conf_menu.add_break()

        url = reverse('admin:pwn_event_place_changelist')
        conf_menu.add_sideframe_item(
            _('Lieux'), url=url,
            disabled=not user.has_perm('pwn_event.change_place'))

        url = reverse('admin:pwn_event_speaker_changelist')
        conf_menu.add_sideframe_item(
            _('Conférenciers'), url=url,
            disabled=not user.has_perm('pwn_event.season_speaker'))

        url = reverse('admin:pwn_event_season_changelist')
        conf_menu.add_sideframe_item(
            _('Saisons'), url=url,
            disabled=not user.has_perm('pwn_event.season_season'))

        conf_menu.add_break()
