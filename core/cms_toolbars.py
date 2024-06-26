from django.contrib.sites.models import Site
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _

from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from cms.cms_toolbars import BasicToolbar
from cms.cms_toolbars import PlaceholderToolbar
from cms.utils.conf import get_cms_setting
from cms.utils.urlutils import admin_reverse

# Identifiers for search
toolbar_pool.unregister(BasicToolbar)
toolbar_pool.unregister(PlaceholderToolbar)

# Identifiers for search
ADMIN_SITES_BREAK = 'Admin Sites Break'
LANGUAGE_MENU_IDENTIFIER = 'language-menu'
CLIPBOARD_BREAK = 'Clipboard Break'
USER_SETTINGS_BREAK = 'User Settings Break'
TOOLBAR_DISABLE_BREAK = 'Toolbar disable Break'
SHORTCUTS_BREAK = 'Shortcuts Break'
ADMINISTRATION_BREAK = 'Administration Break'
ADMIN_MENU_IDENTIFIER = 'admin-menu'
USER_SETTINGS_BREAK = 'User Settings Break'
PWD_BREAK = 'Password Break'

HELP_MENU_IDENTIFIER = 'help-menu'
HELP_MENU_BREAK = 'Help Menu Break'
DEFAULT_HELP_MENU_ITEMS = (
    (gettext("Documentation utilisateur (en ligne) [FR]"), 'https://support.kapt.mobi/index.php/docs/kapt-doc/'),
    (gettext("Guide specifique à votre site (pdf) [FR]"), '/static/core/docs/manuel_utilisateur.pdf'),
)
EXTRA_HELP_MENU_ITEMS = (
    # (gettext(""), 'https://'),
)


@toolbar_pool.register
class PlaceholderToolbarNoWizard(PlaceholderToolbar):
    def add_wizard_button(self):
        pass

@toolbar_pool.register
class CustomToolbarClass(CMSToolbar):
    def populate(self):
        self.toolbar.add_modal_item(
            name='Bibliothèque de medias',
            url='/admin/filer/folder/',
            position=2
        )

@toolbar_pool.register
class CustomBasicToolbar(BasicToolbar):
    """ Herite de BasicToolbar mais retire les menus 'help' et 'language' """


    def populate(self):
        if not self.page:
            self.init_from_request()
            self.clipboard = self.request.toolbar.user_settings.clipboard
            self.add_admin_menu()
            # self.add_language_menu()
            # self.add_help_menu()

    def add_help_menu(self):
        """ Adds the help menu if it's enabled in settings """
        self._help_menu = self.toolbar.get_or_create_menu(HELP_MENU_IDENTIFIER, _('Aide'), position=-1)
        self._help_menu.items = []  # reset the items so we don't duplicate
        for label, url in DEFAULT_HELP_MENU_ITEMS:
            self._help_menu.add_link_item(label, url=url)

        if len(EXTRA_HELP_MENU_ITEMS) > 0:
            self._help_menu.add_break(HELP_MENU_BREAK)

        for label, url in EXTRA_HELP_MENU_ITEMS:
            self._help_menu.add_link_item(label, url=url)

    def add_admin_menu(self):
        if not self._admin_menu:
            self._admin_menu = self.toolbar.get_or_create_menu(ADMIN_MENU_IDENTIFIER, self.current_site.name)
            # Users button
            self.add_users_button(self._admin_menu)

            # sites menu
            sites_queryset = Site.objects.order_by('name')

            if len(sites_queryset) > 1:
                sites_menu = self._admin_menu.get_or_create_menu('sites', _('Sites'))
                sites_menu.add_sideframe_item(_('Admin Sites'), url=admin_reverse('sites_site_changelist'))
                sites_menu.add_break(ADMIN_SITES_BREAK)
                for site in sites_queryset:
                    sites_menu.add_link_item(site.name, url='http://%s' % site.domain,
                                             active=site.pk == self.current_site.pk)

            # admin
            self._admin_menu.add_sideframe_item(_('Administration'), url=admin_reverse('index'))
            self._admin_menu.add_break(ADMINISTRATION_BREAK)

            # cms users settings
            # self._admin_menu.add_sideframe_item(_('User settings'), url=admin_reverse('cms_usersettings_change'))
            # self._admin_menu.add_break(USER_SETTINGS_BREAK)

            # clipboard
            if self.toolbar.edit_mode_active:
                # True if the clipboard exists and there's plugins in it.
                clipboard_is_bound = self.toolbar.clipboard_plugin

                self._admin_menu.add_link_item(
                    _('Clipboard...'), url='#',
                    extra_classes=['cms-clipboard-trigger'],
                    disabled=not clipboard_is_bound
                )
                self._admin_menu.add_link_item(
                    _('Clear clipboard'), url='#',
                    extra_classes=['cms-clipboard-empty'],
                    disabled=not clipboard_is_bound
                )
                self._admin_menu.add_break(CLIPBOARD_BREAK)

            # Disable toolbar
            self._admin_menu.add_link_item(
                _('Disable toolbar'),
                url='?%s' % get_cms_setting('CMS_TOOLBAR_URL__DISABLE')
            )
            self._admin_menu.add_break(TOOLBAR_DISABLE_BREAK)
            self._admin_menu.add_link_item(
                _('Shortcuts...'), url='#',
                extra_classes=('cms-show-shortcuts',)
            )
            self._admin_menu.add_break(SHORTCUTS_BREAK)

            self.add_pwd_button(self._admin_menu)
            self._admin_menu.add_break(PWD_BREAK)

            # logout
            self.add_logout_button(self._admin_menu)

    def add_pwd_button(self, parent):

        user = self.request.user
        if user:
            pwd_change_url = (f'/admin/auth/user/{user.id}/password/')
            parent.add_modal_item(_('Modifier votre mot de passe'), url=pwd_change_url)
