echo "starting board"

currently_running=false
while :;
do
  echo "Top currently_running: $currently_running"
  if [ "$(python3 ./config/should_turn_on.py)" = "True" ]; then
    if [ "$currently_running" = false ]; then
      echo "Starting main.py"
      cd mlb-led-scoreboard/
      sudo python3 main.py --led-gpio-mapping="adafruit-hat" --led-brightness 30 &
      cd ..
      currently_running=true
    fi
  elif [ "$currently_running" = true ]; then
    echo "Killing main.py"
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