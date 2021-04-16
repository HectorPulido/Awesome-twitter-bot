import json
from django.conf import settings
from twitter_data.models import User
from twitter_data.twitter_bot import TwitterBot
from twitter_data.models import User, Feature


def run():
    feature_config = json.loads(Feature.objects.get(name="TWITTER_CONFIG").value)
    sleep_time = feature_config.get("sleep_time", 1)

    bot = TwitterBot(
        settings.CONSUMER_KEY,
        settings.CONSUMER_SECRET,
        settings.ACCESS_TOKEN,
        settings.ACCESS_TOKEN_SECRET,
        sleep_time,
    )

    feature_config = json.loads(Feature.objects.get(name="SEARCH_FOLLOW_TWEETS").value)
    user_groups = feature_config.get("groups", 5)

    # Users
    must_like = User.objects.filter(must_like=True)
    must_retweet = User.objects.filter(must_rt=True)
    print(f"Database: must_like {len(must_like)}, must_retweet {len(must_retweet)}")

    queries_like = bot.build_queries_user_has_link(must_like, user_groups, True)
    queries_retweet = bot.build_queries_user_has_link(must_retweet, user_groups, True)
    print(f"Query: must_like {len(queries_like)}, must_retweet {len(queries_retweet)}")

    tweets_to_like = bot.search_tweets(
        queries_like, ignore_rt=True, result_type="mixed", lang=None
    )
    tweets_to_retweet = bot.search_tweets(
        queries_retweet, ignore_rt=True, result_type="mixed", lang=None
    )
    print(
        f"Tweets: must_like {len(tweets_to_like)}, must_retweet {len(tweets_to_retweet)}"
    )

    bot.retweet(tweets_to_retweet)
    bot.like(tweets_to_like)
    print(f"Users OK")
