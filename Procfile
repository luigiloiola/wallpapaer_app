release: python3 manage.py migrate
web: daphne -u /tmp/daphne.sock wallpaper_app.asgi:application --port $PORT --bind 0.0.0.0 -v2