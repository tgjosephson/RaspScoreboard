import os
local = False

# print(os.getcwd())
# if local:
#     os.chdir('mlb_led_scoreboard')
# print(os.getcwd())

import json
from datetime import datetime
from config.custom import Custom

config_file = open('./config/board-config.json')
config = json.load(config_file)

# Overall power
if config['power'] == 'OFF':
    print("False")
    exit(0)

# Display times
weekno = datetime.today().weekday()
if weekno < 5:
    display_times = config['display_times']['weekday']
else:  # 5 Sat, 6 Sun
    display_times = config['display_times']['weekend']

for time_window in display_times:
    current_time = int(datetime.now().strftime("%H%M"))
    if current_time >= time_window[0] and current_time <= time_window[1]:
        print("True")
        exit(0)

# Preferred team playing
# pref_playing = Custom().is_preferred_team_playing()
# if pref_playing:
#     print("True")
#     exit(0)

print("False")