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

    # Users
    must_like = User.objects.filter(must_like=True)
    must_retweet = User.objects.filter(must_rt=True)
    print(f"Database: must_like {len(must_like)}, must_retweet {len(must_retweet)}")

    queries_like = bot.build_queries_user_has_link(must_like, True)
    queries_retweet = bot.build_queries_user_has_link(must_retweet, True)
    print(f"Query: must_like {len(queries_like)}, must_retweet {len(queries_retweet)}")

    tweets_to_like = bot.search_tweets(queries_like)
    tweets_to_retweet = bot.search_tweets(queries_retweet)
    print(
        f"Tweets: must_like {len(tweets_to_like)}, must_retweet {len(tweets_to_retweet)}"
    )

    bot.retweet(tweets_to_retweet)
    bot.like(tweets_to_like)
    print(f"Users OK")
