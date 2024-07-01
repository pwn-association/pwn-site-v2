from datetime import date

from django.core.management.base import BaseCommand, CommandError
from django.db import connections
from filer.models import Image
from filer.models.foldermodels import Folder
from pwn_event.models import Event, Place, Season, Speaker, Tag

EVENT_START_SEASON_MONTH = 9
EVENT_END_SEASON_MONTH = 7


class Command(BaseCommand):
    """
    Command qui permet de récupérer les conferences (et leurs datas liées) depuis l'ancien site
    """

    help = "Import conferences from old pwn website"

    def handle(self, *args, **options):

        self.create_speakers()
        self.create_tags()
        self.create_conferences()



    def success_message(self, imports_number) -> None:
        """ Affichage du message de succès dans la console """
        self.stdout.write(
            self.style.SUCCESS(f'{imports_number} conference(s) imported successfully')
        )

    def create_conferences(self):
        counter = 0
        with connections["pwn_v1"].cursor() as cursor:
            cursor.execute(self.get_sql())
            rows = cursor.fetchall()

            for row in rows:
                event_date = row[1].strftime("%Y-%m-%d 18:30:00")
                place = self.get_or_create_place(row[10])
                season = self.get_or_create_season(row[1])
                image = self.get_or_create_image(row[11], row[12])

                fields = {
                    "id": row[0],
                    "title": row[6],
                    "slug": row[9],
                    "image": image,
                    "description": row[7],
                    "date": event_date,
                    "place": place,
                    "season": season,
                }

                # Create conferences
                conference = Event(**fields)
                conference.save()

                # Ajout des speakers aux confs
                event_speaker_sql = f"""
                    SELECT event_id, person_id
                    FROM aldryn_events_event_intervenant
                    WHERE event_id = {row[0]}
                    """
                cursor.execute(event_speaker_sql)
                speaker_rows = cursor.fetchall()
                for event_speaker_row in speaker_rows:
                    speaker = Speaker.objects.get(id=event_speaker_row[1])
                    conference.speakers.add(speaker)

                # Ajout des tags aux confs
                event_tags_sql = f"""
                    SELECT object_id, tag_id
                    FROM taggit_taggeditem
                    WHERE content_type_id = 42
                    AND object_id = {row[0]}
                    """
                cursor.execute(event_tags_sql)
                tag_rows = cursor.fetchall()
                for event_tag_row in tag_rows:
                    try:
                        tag = Tag.objects.get(id=event_tag_row[1])
                        conference.tags.add(tag)
                    except Tag.DoesNotExist:
                        pass

                counter += 1
        self.success_message(counter)

    @staticmethod
    def get_sql() -> str:
        """
        Retourne la requête sql (format texte) qui permet de récupérer l'ensembles des données des conférences sur l'ancien site pwn
        """
        return """
                SELECT aldryn_events_event.id,
                aldryn_events_event.start_date,
                aldryn_events_event.start_time,
                aldryn_events_event.detail_link,
                aldryn_events_event.description_id, 
                aldryn_events_event_translation.id,
                aldryn_events_event_translation.title, 
                aldryn_events_event_translation.short_description,
                aldryn_events_event_translation.location,
                aldryn_events_event_translation.slug,
                aldryn_events_event_translation.location,
                filer_file.file,
                filer_file.original_filename        
                FROM aldryn_events_event
                JOIN aldryn_events_event_translation ON aldryn_events_event_translation.master_id = aldryn_events_event.id
                JOIN filer_file ON filer_file.id = aldryn_events_event_translation.image_id 
                WHERE aldryn_events_event.is_published = 't'
            """

    def get_or_create_season(self, event_date: date) -> Season:
        """
        Method get_or_create_season()
        This method is used to get or create a season object based on the provided date.

        Parameters:
        - date: The date for which the season object needs to be fetched or created.

        Returns:
        - season: The season object that was fetched or created.
        """
        season_title, season_start, season_end = self.get_season(event_date)
        try:
            season = Season.objects.get(name=season_title)
        except Season.DoesNotExist:
            season = Season.objects.create(
                name=season_title,
                start_date=season_start,
                end_date=season_end
            )

        return season

    @staticmethod
    def get_or_create_place(place_name: str) -> Place:

        if place_name == "":
            place_name = "-"

        if "Hotel" in place_name:
            place_name = "Hôtel"

        try:
            place = Place.objects.get(name__startswith=place_name[:5])
        except Place.DoesNotExist:
            place = Place.objects.create(name=place_name)

        return place

    def create_speakers(self):
        sql = """            
            SELECT aldryn_people_person_translation.name,
            aldryn_people_person_translation.slug,   
            aldryn_people_person_translation.description,           
            aldryn_people_person.website,
            aldryn_people_person.id
            FROM aldryn_people_person_translation
            JOIN aldryn_people_person ON aldryn_people_person_translation.master_id = aldryn_people_person.id
            """

        with connections["pwn_v1"].cursor() as cursor:
            cursor.execute(sql)
            rows = cursor.fetchall()

            for row in rows:
                name = row[0].split(" ")
                if len(name) == 1:
                    name.append('-')

                fields = {
                    'id': row[4],
                    'first_name': name[0],
                    'last_name': name[1],
                    'slug': row[1],
                    'biography': row[2],
                    'url': row[3],
                }

                # Create speaker
                conference = Speaker(**fields)
                conference.save()

    def create_tags(self):
        sql = """SELECT id, name, slug FROM taggit_tag"""

        with connections["pwn_v1"].cursor() as cursor:
            cursor.execute(sql)
            rows = cursor.fetchall()

            for row in rows:
                fields = {
                    'id': row[0],
                    'name': row[1],
                    'slug': row[2]
                }

                # Create speaker
                tag = Tag(**fields)
                tag.save()

    @staticmethod
    def get_or_create_image(image_url: str, image_name: str) -> Image:
        folder = Folder.objects.get(id=1)
        image = Image(file=image_url, original_filename=image_name, folder=folder)
        image.save()
        return image

    @staticmethod
    def get_season(event_date: date) -> (str, date, date):
        """
        Get the season based on the event date.

        Parameters:
        - event_date (date): The date of the event.

        Returns:
        - season (str): The season in the format "saison <year> - <year+1>".
        - season_start (date): The start date of the season.
        - season_end (date): The end date of the season.
        """

        season_start = season_end = season = None
        current_year = event_date.year
        current_month = event_date.month

        # debut / fin de saison
        if current_month < EVENT_START_SEASON_MONTH:
            season = "saison %s - %s" % (current_year - 1, current_year)
            season_start = date(current_year-1, EVENT_START_SEASON_MONTH, 1)
            season_end = date(current_year, EVENT_END_SEASON_MONTH, 1)

        if current_month > EVENT_END_SEASON_MONTH:
            season = "saison %s - %s" % (current_year, current_year + 1)
            season_start = date(current_year, EVENT_START_SEASON_MONTH, 1)
            season_end = date(current_year + 1, EVENT_END_SEASON_MONTH, 1)

        return season, season_start, season_end
