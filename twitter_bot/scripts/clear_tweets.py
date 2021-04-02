from twitter_data.models import Tweet


def run():
    tweets = Tweet.objects.filter(retweeted=True) | Tweet.objects.filter(liked=True)
    tweets.delete()
