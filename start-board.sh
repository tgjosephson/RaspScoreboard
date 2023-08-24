exit 0

echo "starting board"
python3 main.py
cd mlb-led-scoreboard/

currently_running=false
while :;
do
  current_date_time=$(date +%H%M)
  echo "Current date and time: $current_date_time"
  echo "Top currently_running: $currently_running"
  if [ "$current_date_time" -ge 0700 -a "$current_date_time" -le 2200 ]; then
    if [ "$currently_running" = false ]; then
      echo "Starting main.py"
      sudo python3 main.py --led-gpio-mapping="adafruit-hat" --led-brightness 30 &
      currently_running=true
    fi
  elif [ "$currently_running" = true ]; then
    echo "Killing main.py"
    sudo pkill -f main.py
    sudo reboot
    currently_running=false
  fi
  echo "Bottom currently_running: $currently_running"
  sleep 30
done

echo "end"
sleep 5
exit 0