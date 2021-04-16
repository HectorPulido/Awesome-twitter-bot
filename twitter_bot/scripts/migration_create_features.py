import json
from twitter_data.models import Feature


def run():
    users_to_delete = "USERS_TO_DELETE"
    users_to_delete_data = {"min_retweets": 5, "count": 1000}

    users_to_follow = "USERS_TO_FOLLOW"
    users_to_follow_data = {"min_retweets": 5, "min_retweets_to_like": 10}

    tweets_to_delete = "TWEETS_TO_DELETE"
    tweets_to_delete_data = {"count": 1000}

    search_follow_tweets = "SEARCH_FOLLOW_TWEETS"
    search_follow_tweets_data = {"groups": 1}

    twitter_config = "TWITTER_CONFIG"
    twitter_config_data = {
        "sleep_time": 5,
        "search_ignore_rt": True,
        "result_type": "recent",
        "lang": "es",
    }

    Feature.objects.create(name=users_to_delete, value=json.dumps(users_to_delete_data))
    Feature.objects.create(name=users_to_follow, value=json.dumps(users_to_follow_data))
    Feature.objects.create(
        name=tweets_to_delete, value=json.dumps(tweets_to_delete_data)
    )
    Feature.objects.create(
        name=search_follow_tweets, value=json.dumps(search_follow_tweets_data)
    )
    Feature.objects.create(name=twitter_config, value=json.dumps(twitter_config_data))
