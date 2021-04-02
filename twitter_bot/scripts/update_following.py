from django.conf import settings
from twitter_data.models import User
from twitter_data.twitter_bot import TwitterBot


def run():
    bot = TwitterBot(
        settings.CONSUMER_KEY,
        settings.CONSUMER_SECRET,
        settings.ACCESS_TOKEN,
        settings.ACCESS_TOKEN_SECRET,
        1,
    )
    must_follow = User.objects.filter(must_follow=True, followed=False)
    bot.follow(must_follow)
    must_unfollow = User.objects.filter(must_follow=False, followed=True)
    bot.unfollow(must_unfollow)
