from django.contrib import admin
from .models.event import Event
from .models.speaker import Speaker
from .models.place import Place
from .models.season import Season


class EventAdmin(admin.ModelAdmin):
    pass


class SpeakerAdmin(admin.ModelAdmin):
    pass


class PlaceAdmin(admin.ModelAdmin):
    pass


class SeasonAdmin(admin.ModelAdmin):
    pass


admin.site.register(Event, EventAdmin)
admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Season, SeasonAdmin)
