echo "starting board"

currently_running=false
while :;
do
  echo "Top currently_running: $currently_running"
  if [ "$(python3 ./should_turn_on.py)" = "True" ]; then
    if [ "$currently_running" = false ]; then
      echo "Starting main.py"
      cd nhl_led_scoreboard/
      sudo python3 src/main.py --led-gpio-mapping="adafruit-hat" --led-slowdown-gpio=2 &
      cd ..
      currently_running=true
    fi
  elif [ "$currently_running" = true ]; then
    echo "Killing main.py"
    sudo pkill -f src/main.py
    sudo reboot
    currently_running=false
  fi
  echo "Bottom currently_running: $currently_running"
  sleep 5
done

echo "end"
sleep 5
exit 0