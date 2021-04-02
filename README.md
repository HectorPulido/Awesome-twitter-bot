# twitter_bot

docker build -t web:latest .
docker run -d --name django-heroku -e "PORT=8765" -e "DEBUG=0" -p 8007:8765 web:latest
docker start django-heroku
docker stop django-heroku
docker rm django-heroku

docker build -t pequenin-twitter .
docker run -d --name pequenin-twitter -e "PORT=8765" -e "DEBUG=0" -p 8007:8765 web:latest
heroku container:login
heroku container:push web -a pequenin-twitter
heroku container:release web -a pequenin-twitter
heroku run python manage.py migrate -a pequenin-twitter 
heroku run python manage.py runscript search_tweets -a pequenin-twitter 

https://elements.heroku.com/addons/scheduler