from django.conf import settings
from twitter_data.models import User


def run():
    for row in User.objects.all().reverse():
        if User.objects.filter(user_profile=row.user_profile).count() > 1:
            row.delete()
