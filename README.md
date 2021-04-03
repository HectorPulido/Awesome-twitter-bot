# Awesome Twitter Bot

This is a tweepy/django/heroku/heroku-postgres/dropbox based twitter bot, it can follow, search, like, and ignore people from twitter, contains an advance admin to personalize it.

You can follow this bot here: https://twitter.com/PequeninWarior

## Features
- Follow/Unfollow, Like, Retweet and Search 
- Customizable topics, people, etc from django admin
- Heroku free tier full support
- Save the data in .csv format in dropbox
- Automated actions

## TODO
- Machine learning for tweet classification
- Responses
- Less intrusive algorithm

## How it works
This is a heroku based project

### Setup Django

1. Configure your heroku project, save the name, you will need the Heroku Postgres and Heroku Scheduler add-ons
2. Configure the environment variables from the heroku settings
```
THIS FROM TWITTER https://developer.twitter.com/en
CONSUMER_KEY = "nC9waTEqsOxkYu4knDntrEwZY"
CONSUMER_SECRET = "GTGCCfXBgtRdT6xGeJJZY9vvW0EPKUnZoJdRLTmy1SiJuj6GUa"
ACCESS_TOKEN = "1377810525845880840-lyv2qHifb5Iaf3qxa4f0d101DoVjXo"
ACCESS_TOKEN_SECRET = "xJi6KuIajRXnT8AdiYFjiVYR9voGSo03pXgasExPlA0E2"

THIS FROM DROPBOX (Optional) https://www.dropbox.com/lp/developers
ACCESS_TOKEN_DROPBOX="sl.AuPLMZPcqnK0HBe-FG0WowJN_bRQectMgmaBsTAxJI1Yn9HnMWU8hYstrnA9zL60F3c0GQvlnzB7n9QXboW0uw0k04-dV4y6twhKTY4zWzgSo7ARdp0H6OoBBlIq0hYBGeLYUxY"

DEBUG = 1
SECRET_KEY a random string 
```

3. Build the docker development and run it to make sure everything is ok

```
docker build -t web:latest .
docker run -d --name <herokuname> -e "PORT=8765" -e "DEBUG=0" -p 8007:8765 web:latest
```
4. You can deactivate like this
```
docker stop <herokuname>
docker rm <herokuname>
```
5. You can upload your project with this commands
```
docker run -d --name <herokuname> -e "PORT=8765" -e "DEBUG=0" -p 8007:8765 web:latest
heroku container:login
heroku container:push web -a <herokuname>
heroku container:release web -a <herokuname>
```
6. Do not forget to migrate
```
heroku run python manage.py migrate -a <herokuname>
```

7. Create your user with
```
heroku run python manage.py createsuperuser -a <herokuname>
```

8. Enter to your proyect from this url
```
http://<herokuname>.herokuapp.com/admin
```

9. Enter to your proyect from this url
```
http://<herokuname>.herokuapp.com/admin
```

10. Log in and configure your interest topics and interest users

11. You can try this commands
```
heroku run python manage.py runscript update_following -a <herokuname>
heroku run python manage.py runscript search_follow_tweets -a <herokuname>
heroku run python manage.py runscript search_tweets -a <herokuname>
```

12. Configure your scheduler with those commands

13. You are ready


## More interesting projects
I have a lot of fun projects, check this:

### Machine learning
- https://github.com/HectorPulido/Evolutionary-Neural-Networks-on-unity-for-bots
- https://github.com/HectorPulido/Imitation-learning-in-unity
- https://github.com/HectorPulido/Chatbot-seq2seq-C-

### Games
- https://github.com/HectorPulido/Unity-MMO-Framework
- https://github.com/HectorPulido/Contra-Like-game-made-with-unity
- https://github.com/HectorPulido/Pacman-Online-made-with-unity

### Random
- https://github.com/HectorPulido/Arithmetic-Parser-made-easy
- https://github.com/HectorPulido/Simple-php-blog
- https://github.com/HectorPulido/Decentralized-Twitter-with-blockchain-as-base


## Licence
This proyect uses Django, tweepy, dropbox libraries, also was made to work with heroku but everything else was totally handcrafted by me, so the licence is MIT, use it as you want.

<div align="center">
<h3 align="center">Let's connect 😋</h3>
</div>
<p align="center">
<a href="https://www.linkedin.com/in/hector-pulido-17547369/" target="blank">
<img align="center" width="30px" alt="Hector's LinkedIn" src="https://www.vectorlogo.zone/logos/linkedin/linkedin-icon.svg"/></a> &nbsp; &nbsp;
<a href="https://twitter.com/Hector_Pulido_" target="blank">
<img align="center" width="30px" alt="Hector's Twitter" src="https://www.vectorlogo.zone/logos/twitter/twitter-official.svg"/></a> &nbsp; &nbsp;
<a href="https://www.twitch.tv/hector_pulido_" target="blank">
<img align="center" width="30px" alt="Hector's Twitch" src="https://www.vectorlogo.zone/logos/twitch/twitch-icon.svg"/></a> &nbsp; &nbsp;
<a href="https://www.youtube.com/channel/UCS_iMeH0P0nsIDPvBaJckOw" target="blank">
<img align="center" width="30px" alt="Hector's Youtube" src="https://www.vectorlogo.zone/logos/youtube/youtube-icon.svg"/></a> &nbsp; &nbsp;
