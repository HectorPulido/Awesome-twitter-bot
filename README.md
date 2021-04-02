# twitter_bot

docker build -t web:latest .
docker run -d --name django-heroku -e "PORT=8765" -e "DEBUG=0" -p 8007:8765 web:latest
docker start django-heroku
docker stop django-heroku
docker rm django-heroku

docker build -t registry.heroku.com/pequenin-twitter/web .

heroku container:

heroku registry.heroku.com/pequenin-twitter/web:login

heroku container:release -a pequenin-twitter web



eroku run python manage.py makemigrations -a pequenin-twitter

heroku run python manage.py migrate -a pequenin-twitter


heroku run python manage.py createsuperuser -a pequenin-twitter