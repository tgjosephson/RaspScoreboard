from datetime import datetime, timedelta
import os
import json
from mlb_led_scoreboard import debug
from collections.abc import Mapping

def parse_today(end_of_day):
    today = datetime.today()
    end_of_day = datetime.strptime(end_of_day, "%H:%M").replace(
        year=today.year, month=today.month, day=today.day
    )
    if end_of_day > datetime.now():
        today -= timedelta(days=1)
    return today 

def filter_list_of_games(games, preferred_teams):
    teams = [TEAM_FULL[t] for t in preferred_teams]
    return list(game for game in games if set([game["away_name"], game["home_name"]]).intersection(set(teams)))

# example config is a "base config" which always gets read.
# our "custom" config contains overrides.
def get_config(base_filename):
    filename = "{}.json".format(base_filename)
    reference_filename = "config.json.example"  # always use this filename.
    reference_config = read_json(reference_filename)
    custom_config = read_json(filename)
    if custom_config:
        new_config = deep_update(reference_config, custom_config)
        return new_config
    return reference_config

def deep_update(source, overrides):
    """Update a nested dictionary or similar mapping.
    Modify ``source`` in place.
    """
    for key, value in list(overrides.items()):
        if isinstance(value, Mapping) and value:
            returned = deep_update(source.get(key, {}), value)
            source[key] = returned
        else:
            source[key] = overrides[key]
    return source

def read_json(path):
    """
    Read a file expected to contain valid json.
    If file not present return empty data.
    Exception if json invalid.
    """
    j = {}
    if os.path.isfile(path):
        j = json.load(open(path))
    else:
        debug.info(f"Could not find json file {path}.  Skipping.")
    return j

TEAM_FULL = {
    "Athletics": "Oakland Athletics",
    "Pirates": "Pittsburgh Pirates",
    "Padres": "San Diego Padres",
    "Mariners": "Seattle Mariners",
    "Giants": "San Francisco Giants",
    "Cardinals": "St. Louis Cardinals",
    "Rays": "Tampa Bay Rays",
    "Rangers": "Texas Rangers",
    "Blue Jays": "Toronto Blue Jays",
    "Twins": "Minnesota Twins",
    "Phillies": "Philadelphia Phillies",
    "Braves": "Atlanta Braves",
    "White Sox": "Chicago White Sox",
    "Marlins": "Miami Marlins",
    "Yankees": "New York Yankees",
    "Brewers": "Milwaukee Brewers",
    "Angels": "Los Angeles Angels",
    "D-backs": "Arizona Diamondbacks",
    "Orioles": "Baltimore Orioles",
    "Red Sox": "Boston Red Sox",
    "Cubs": "Chicago Cubs",
    "Reds": "Cincinnati Reds",
    "Guardians": "Cleveland Guardians",
    "Rockies": "Colorado Rockies",
    "Tigers": "Detroit Tigers",
    "Astros": "Houston Astros",
    "Royals": "Kansas City Royals",
    "Dodgers": "Los Angeles Dodgers",
    "Nationals": "Washington Nationals",
    "Mets": "New York Mets",
}

TEAM_ABBR_LN = {
    "Oakland Athletics": "OAK",
    "Pittsburgh Pirates": "PIT",
    "San Diego Padres": "SD",
    "Seattle Mariners": "SEA",
    "San Francisco Giants": "SF",
    "St. Louis Cardinals": "STL",
    "Tampa Bay Rays": "TB",
    "Texas Rangers": "TEX",
    "Toronto Blue Jays": "TOR",
    "Minnesota Twins": "MIN",
    "Philadelphia Phillies": "PHI",
    "Atlanta Braves": "ATL",
    "Chicago White Sox": "CWS",
    "Miami Marlins": "MIA",
    "New York Yankees": "NYY",
    "Milwaukee Brewers": "MIL",
    "Los Angeles Angels": "LAA",
    "Arizona Diamondbacks": "AZ",
    "Baltimore Orioles": "BAL",
    "Boston Red Sox": "BOS",
    "Chicago Cubs": "CHC",
    "Cincinnati Reds": "CIN",
    "Cleveland Guardians": "CLE",
    "Colorado Rockies": "COL",
    "Detroit Tigers": "DET",
    "Houston Astros": "HOU",
    "Kansas City Royals": "KC",
    "Los Angeles Dodgers": "LAD",
    "Washington Nationals": "WSH",
    "New York Mets": "NYM",
}
