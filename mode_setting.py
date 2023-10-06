import json

config_file = open('./config/board-config.json')
config = json.load(config_file)

print(config['mode'])
exit(0)