from django.contrib import admin
from .models.event import Event
from .models.speaker import Speaker
from .models.place import Place
from .models.season import Season
from .models.tag import Tag


class EventAdmin(admin.ModelAdmin):
    date_hierarchy = "date"
    list_filter = ['is_publish', 'season']
    search_fields = ['title', 'speakers__first_name', 'speakers__last_name',]
    list_display = ['title', 'is_publish', 'date', 'season', 'get_speakers', 'place',]
    readonly_fields = ('season',)
    fieldsets =  [
        (
            None,
            {
                "fields": [
                    ("title", "is_publish"),
                    "season", "place",
                    "date",  "image", "description", "tags",

                ],
            },
        ),
        # (
        #     "Description / Image",
        #     {
        #         "classes": ["collapse"],
        #         "fields": ["image", "description",],
        #     },
        # ),
        (
            "Speakers",
            {
                "classes": ["collapse"],
                "fields": ["speakers"],
            },
        ),
        # (
        #     "Tags / Catégories",
        #     {
        #         "classes": ["collapse"],
        #         "fields": ["tags"],
        #     },
        # ),
        (
            "Publication",
            {
                "classes": ["collapse"],
                "fields": ["n8n", "start_publication", "end_publication"],
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
    fieldsets = [
            (
                None,
                {
                    "fields": [
                        ("first_name", "last_name"),
                        "biography", "url"
                    ],
                },
            ),
        ]

class PlaceAdmin(admin.ModelAdmin):
    fieldsets = [
            (
                None,
                {
                    "fields": [
                        "name",
                    ],
                },
            ),
            (
                "Adresse",
                {
                    "fields": [
                        "address", "address2", "zip", "city",
                    ],
                },
            ),
        ]


class SeasonAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date']


class TagAdmin(admin.ModelAdmin):
    pass


admin.site.register(Event, EventAdmin)
admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Season, SeasonAdmin)
admin.site.register(Tag, TagAdmin)
