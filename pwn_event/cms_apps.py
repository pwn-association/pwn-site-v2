from abc import ABC

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import gettext_lazy as _


@apphook_pool.register
class ConferenceApphook(CMSApp, ABC):
    name = _("Conférences")
    app_name = "conference"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["pwn_event.urls"]

    @property
    def urls(self):
        return self.get_urls()
