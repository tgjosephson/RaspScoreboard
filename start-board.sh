echo "starting board"

config_file = open('./config/board-config.json')
config = json.load(config_file)

currently_running=false
while :;
do
  echo "Top currently_running: $currently_running"
  if [ "$(python3 ./should_turn_on.py)" = "True" ]; then
    if [ "$currently_running" = false ]; then
      echo "Starting board"
      if config['mode'] == 'nhl':
        cd nhl_led_scoreboard/
        sudo python3 src/main.py --led-gpio-mapping="adafruit-hat" --led-slowdown-gpio=2 &
      elif config['mode'] == 'mlb':
        cd mlb_led_scoreboard/
        sudo python3 main.py --led-gpio-mapping="adafruit-hat" --led-brightness 30 &
      cd ..
      currently_running=true
    fi
  elif [ "$currently_running" = true ]; then
    echo "Killing board"
    if config['mode'] == 'nhl':
      sudo pkill -f src/main.py
    elif config['mode'] == 'mlb':
      sudo pkill -f main.py
    sudo reboot
    currently_running=false
  fi
  echo "Bottom currently_running: $currently_running"
  sleep 5
done

echo "end"
sleep 5
exit 0