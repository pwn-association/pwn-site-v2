from django.contrib import admin
from .models.event import Event
from .models.speaker import Speaker
from .models.place import Place
from .models.season import Season
from .models.tag import Tag


class EventAdmin(admin.ModelAdmin):
    date_hierarchy = "date"
    list_filter = ['is_publish',]
    search_fields = ['title', 'speakers__first_name', 'speakers__last_name',]
    list_display = ['title', 'date', 'get_speakers', 'place', 'is_publish']
    fieldsets =  [
        (
            None,
            {
                "fields": [
                    ("title", "is_publish"),
                    "date",
                    "image", "excerpt", "description",
                    "place", "speakers", "tags",
                    "season",
                ],
            },
        ),
        (
            "Publication",
            {
                "classes": ["collapse"],
                "fields": ["start_publication", "end_publication"],
            },
        ),
    ]
    filter_horizontal = ('tags', 'speakers')

    def get_speakers(self, obj):
        intervenant = ''
        for speaker in obj.speakers.all():
            intervenant += f"{speaker.first_name} {speaker.last_name}"
        return intervenant


class SpeakerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', ]
    search_fields = ['first_name', 'last_name', ]


class PlaceAdmin(admin.ModelAdmin):
    pass


class SeasonAdmin(admin.ModelAdmin):
    pass


class TagAdmin(admin.ModelAdmin):
    pass


admin.site.register(Event, EventAdmin)
admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Season, SeasonAdmin)
admin.site.register(Tag, TagAdmin)
