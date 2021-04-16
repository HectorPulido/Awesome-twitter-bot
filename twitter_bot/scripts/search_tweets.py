import json
from django.conf import settings
from twitter_data.models import Topic, Feature
from twitter_data.twitter_bot import TwitterBot


def run():
    feature_config = json.loads(Feature.objects.get(name="TWITTER_CONFIG").value)
    sleep_time = feature_config.get("sleep_time", 1)
    search_ignore_rt = feature_config.get("search_ignore_rt", True)
    result_type = feature_config.get("result_type", "recent")
    lang = feature_config.get("lang", "es")

    bot = TwitterBot(
        settings.CONSUMER_KEY,
        settings.CONSUMER_SECRET,
        settings.ACCESS_TOKEN,
        settings.ACCESS_TOKEN_SECRET,
        sleep_time,
    )

    # Tweet search
    topics_to_like = Topic.objects.filter(must_like=True)
    topics_to_retweet = Topic.objects.filter(must_rt=True)
    print(
        f"Database: must_like {len(topics_to_like)}, must_retweet {len(topics_to_retweet)}"
    )

    topic_queries_to_like = [
        bot.build_query_with_keywords(
            topic.keywords, topic.ignore_rt, topic.only_links, topic.lang
        )
        for topic in topics_to_like
    ]

    topics_queries_to_retweet = [
        bot.build_query_with_keywords(
            topic.keywords, topic.ignore_rt, topic.only_links, topic.lang
        )
        for topic in topics_to_retweet
    ]

    print(
        f"Query: must_like {len(topic_queries_to_like)}, must_retweet {len(topics_queries_to_retweet)}"
    )

    topics_tweets_to_like = bot.search_tweets(
        topic_queries_to_like, search_ignore_rt, result_type, lang
    )
    topics_tweets_to_retweet = bot.search_tweets(
        topics_queries_to_retweet, search_ignore_rt, result_type, lang
    )

    print(
        f"Tweets: must_like {len(topics_tweets_to_like)}, must_retweet {len(topics_tweets_to_retweet)}"
    )

    bot.retweet(topics_tweets_to_retweet)
    bot.like(topics_tweets_to_like)
