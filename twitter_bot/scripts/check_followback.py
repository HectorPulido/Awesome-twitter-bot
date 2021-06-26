import json
from django.conf import settings
from twitter_data.models import User, Feature
from twitter_data.twitter_bot import TwitterBot
from datetime import datetime, timedelta


def run():
    feature_config = json.loads(Feature.objects.get(name="TWITTER_CONFIG").value)
    sleep_time = feature_config.get("sleep_time", 1)

    feature_config = json.loads(Feature.objects.get(name="FOLLOW_BACK").value)
    check_time_days = int(feature_config.get("check_time_days", 7))
    users_to_check = int(feature_config.get("users_to_check", 20))

    bot = TwitterBot(
        settings.CONSUMER_KEY,
        settings.CONSUMER_SECRET,
        settings.ACCESS_TOKEN,
        settings.ACCESS_TOKEN_SECRET,
        sleep_time,
    )

    a_week_ago = datetime.now() - timedelta(days=check_time_days)
    check_follow_back = User.objects.filter(
        priority=False, created_at__lte=a_week_ago
    ).order_by("?")[:users_to_check]

    bot.get_followers()

    for user in check_follow_back:
        if not bot.check_follow_back(user.user_profile):
            user.must_follow = False
            user.must_like = False
            user.must_rt = False
            user.save()
