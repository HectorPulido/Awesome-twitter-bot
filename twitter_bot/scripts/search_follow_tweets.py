import json
from django.conf import settings
from twitter_data.models import User
from twitter_data.twitter_bot import TwitterBot
from twitter_data.models import User, Feature


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

    feature_config = Feature.get_feature("SEARCH_FOLLOW_TWEETS")
    user_groups = feature_config.get("groups", 5)
    user_to_select = feature_config.get("select", 5)

    # Users
    must_like = (
        User.objects.filter(must_like=True, must_rt=False, priority=True)
        | User.objects.filter(must_like=True, must_rt=False, priority=False).order_by(
            "?"
        )[:user_to_select]
    )
    must_retweet = (
        User.objects.filter(must_like=False, must_rt=True, priority=True)
        | User.objects.filter(must_rt=True, must_like=False, priority=False).order_by(
            "?"
        )[:user_to_select]
    )
    must_rt_like = (
        User.objects.filter(must_like=True, must_rt=True, priority=True)
        | User.objects.filter(must_rt=True, must_like=True, priority=False).order_by(
            "?"
        )[:user_to_select]
    )
    print(
        f"Database: must_like {len(must_like)}, must_retweet {len(must_retweet)}, must rt + like {len(must_rt_like)}"
    )

    queries_like = bot.build_queries_user_has_link(must_like, user_groups, True)
    queries_retweet = bot.build_queries_user_has_link(must_retweet, user_groups, True)
    queries_rt_like = bot.build_queries_user_has_link(must_rt_like, user_groups, True)
    print(
        f"Query: must_like {len(queries_like)}, must_retweet {len(queries_retweet)}, must rt + like {len(queries_rt_like)}"
    )

    tweets_to_like = bot.search_tweets(
        queries_like, ignore_rt=True, result_type="mixed", lang=None
    )
    tweets_to_retweet = bot.search_tweets(
        queries_retweet, ignore_rt=True, result_type="mixed", lang=None
    )
    tweets_to_like_rt = bot.search_tweets(
        queries_rt_like, ignore_rt=True, result_type="mixed", lang=None
    )
    print(
        f"Tweets: must_like {len(tweets_to_like)}, must_retweet {len(tweets_to_retweet)}, must rt + like {len(tweets_to_like_rt)}"
    )

    bot.retweet(tweets_to_retweet)
    bot.like(tweets_to_like)

    bot.retweet(tweets_to_like_rt)
    bot.like(tweets_to_like_rt)
    print(f"Users OK")
