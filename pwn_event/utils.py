import calendar
from datetime import date
from .models.season import Season

EVENT_START_SEASON_MONTH = 9
EVENT_END_SEASON_MONTH = 8


def get_last_day_of_month(year: int, month: int) -> int:
    return calendar.monthrange(year, month)[1]


def get_season(event_date: date) -> (str, date, date):
    """
    Get the season based on the event date.

    Parameters:
    - event_date (date): The date of the event.

    Returns:
    - season_title (str): The season in the format "saison <year> - <year+1>".
    - season_start (date): The start date of the season.
    - season_end (date): The end date of the season.
    """

    season_start = season_end = season = None
    current_year = event_date.year
    current_month = event_date.month

    # debut / fin de saison
    if current_month < EVENT_START_SEASON_MONTH:
        season = "saison %s - %s" % (current_year - 1, current_year)
        season_start = date(current_year - 1, EVENT_START_SEASON_MONTH, 1)
        last_day_month = get_last_day_of_month(current_year, EVENT_END_SEASON_MONTH)
        season_end = date(current_year, EVENT_END_SEASON_MONTH, last_day_month)

    if current_month > EVENT_END_SEASON_MONTH:
        season = "saison %s - %s" % (current_year, current_year + 1)
        season_start = date(current_year, EVENT_START_SEASON_MONTH, 1)
        last_day_month = get_last_day_of_month(current_year, EVENT_END_SEASON_MONTH)
        season_end = date(current_year + 1, EVENT_END_SEASON_MONTH, last_day_month)

    return season, season_start, season_end


def get_or_create_season(event_date: date) -> Season:
    """
    Method get_or_create_season()
    This method is used to get or create a season object based on the provided date.

    Parameters:
    - date: The date for which the season object needs to be fetched or created.

    Returns:
    - season: The season object that was fetched or created.
    """
    season_title, season_start, season_end = get_season(event_date)
    try:
        season = Season.objects.get(start_date=season_start)
    except Season.DoesNotExist:
        season = Season.objects.create(
            name=season_title,
            start_date=season_start,
            end_date=season_end
        )

    return season
