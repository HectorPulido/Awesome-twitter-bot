import json
from twitter_data.models import User, Features


def run():
    feature_config = json.loads(Features.objects.get(name="USERS_TO_FOLLOW").value)

    users = User.objects.filter(
        ignore=False, retweet_count__gte=feature_config.get("min_retweets", 5)
    )

    users.update(must_follow=True)

    users_to_like = User.objects.filter(
        must_follow=True,
        retweet_count__gte=feature_config.get("min_retweets_to_like", 10),
    )
    users_to_like.update(must_like=True, must_rt=True)
