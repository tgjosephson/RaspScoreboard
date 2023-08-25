import json
from datetime import datetime

config_file = open('./config/board-config.json')
config = json.load(config_file)

if config['power'] == 'OFF':
    print("False")
    exit(0)

for time_window in config['display_times']:
    current_time = int(datetime.now().strftime("%H%M"))
    if current_time > time_window[0] and current_time < time_window[1]:
        print("True")
        exit(0)

print("False")