import json
from django.conf import settings
from twitter_data.models import User, Feature
from twitter_data.twitter_bot import TwitterBot


def run():
    feature_config = Feature.get_feature("TWITTER_CONFIG")
    sleep_time = feature_config.get("sleep_time", 1)

    bot = TwitterBot(
        settings.CONSUMER_KEY,
        settings.CONSUMER_SECRET,
        settings.ACCESS_TOKEN,
        settings.ACCESS_TOKEN_SECRET,
        sleep_time,
    )
    must_follow = User.objects.filter(must_follow=True, followed=False)
    bot.follow(must_follow)

    must_unfollow = User.objects.filter(must_follow=False, followed=True)
    bot.unfollow(must_unfollow)
