import json
import requests
import urllib.parse
from django.conf import settings
from twitter_data.twitter_bot import TwitterBot
from twitter_data.models import Feature


def get_response(text, endpoint, api_name, api_key):
    text = urllib.parse.quote(text)
    url = f"{endpoint}phrase/{text}/"

    payload = json.dumps({"name": api_name, "private_key": api_key})

    headers = {"Content-Type": "application/json"}

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def run():
    respond_config = Feature.get_feature("RESPOND_CONFIG")
    if not respond_config:
        return

    endpoint = respond_config.get("endpoint")
    api_name = respond_config.get("api_name")
    api_key = respond_config.get("api_key")

    feature_config = Feature.get_feature("TWITTER_CONFIG")
    sleep_time = feature_config.get("sleep_time", 1)

    bot = TwitterBot(
        settings.CONSUMER_KEY,
        settings.CONSUMER_SECRET,
        settings.ACCESS_TOKEN,
        settings.ACCESS_TOKEN_SECRET,
        sleep_time,
    )

    twits = bot.get_mentions()

    screen_name = bot.api.me().screen_name.lower()
    me = f"@{screen_name}"

    for twit in twits:
        if twit.text.lower().startswith(me) and not twit.replied:
            text = twit.text.lower().replace(me, "").strip()
            response = get_response(text, endpoint, api_name, api_key)[1:-1]
            bot.respond_twit(twit, response)
