from django.conf import settings
from twitter_data.models import User, Topic
from twitter_data.twitter_bot import TwitterBot


def run():
    users = User.objects.all()
    for user in users:
        user.user_profile = user.user_profile.lower()
        user.save()
