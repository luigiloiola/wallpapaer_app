release: python manage.py makemigrations && python manage.py migrate
web: daphne wallpaper_app.asgi:application --port $PORT --bind 0.0.0.0 -v2