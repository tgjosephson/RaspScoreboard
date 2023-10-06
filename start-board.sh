echo "starting board"

mode_setting="$(python3 ./mode_setting.py)"

currently_running=false
while :;
do
  echo "Top currently_running: $currently_running"
  if [ "$(python3 ./should_turn_on.py)" = "True" ]; then
    if [ "$currently_running" = false ]; then
      echo "Starting board"
      if [ "$mode_setting" = 'nhl' ]; then
        cd nhl_led_scoreboard/
        sudo python3 src/main.py --led-gpio-mapping="adafruit-hat" --led-slowdown-gpio=2 &
      elif [ "$mode_setting" = 'mlb' ]; then
        cd mlb_led_scoreboard/
        sudo python3 main.py --led-gpio-mapping="adafruit-hat" --led-cols 64 &
      fi
      cd ..
      currently_running=true
    fi
  elif [ "$currently_running" = true ]; then
    echo "Killing board"
    if [ "$mode_setting" = 'nhl' ]; then
      sudo pkill -f src/main.py
    elif [ "$mode_setting" = 'mlb' ]; then
      sudo pkill -f main.py
    fi
    sudo reboot
    currently_running=false
  fi
  echo "Bottom currently_running: $currently_running"
  sleep 5
done

echo "end"
sleep 5
exit 0