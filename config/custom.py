import statsapi
from datetime import datetime
from config import custom_utils

class Custom:
    def __init__(self):
        json = custom_utils.get_config('./mlb_led_scoreboard/config')
        end_of_day = json["end_of_day"]
        preferred_teams = json["preferred"]["teams"]

        date = custom_utils.parse_today(end_of_day)
        try:
            all_games = statsapi.schedule(date.strftime("%Y-%m-%d"))
        except:
            print("Exception when getting all games from statsapi")

        self.preferred_games = custom_utils.filter_list_of_games(all_games, preferred_teams)


    def is_preferred_team_playing(self):
        current_time = datetime.utcnow()
        for game in self.preferred_games:
            game_time = datetime.strptime(game["game_datetime"], '%Y-%m-%dT%H:%M:%Sz')
            timedelta = game_time - current_time
            if timedelta.days < 0 or (timedelta.seconds)/60 < 120:
                return True
