from django.conf import settings
from twitter_data.models import User, Topic
from twitter_data.twitter_bot import TwitterBot


def run():
    bot = TwitterBot(
        settings.CONSUMER_KEY,
        settings.CONSUMER_SECRET,
        settings.ACCESS_TOKEN,
        settings.ACCESS_TOKEN_SECRET,
        1,
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

    topics_tweets_to_like = bot.search_twits(topic_queries_to_like)
    topics_tweets_to_retweet = bot.search_twits(topics_queries_to_retweet)

    print(
        f"Tweets: must_like {len(topics_tweets_to_like)}, must_retweet {len(topics_tweets_to_retweet)}"
    )

    bot.retweet(topics_tweets_to_retweet)
    bot.like(topics_tweets_to_like)
