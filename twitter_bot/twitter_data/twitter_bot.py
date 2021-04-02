import tweepy
import time
from .models import User, Tweet


class TwitterBot:
    def __init__(
        self,
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret,
        sleep_time,
    ):
        self.sleep_time = sleep_time

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(
            auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True
        )

    def sent_twit(self, twit_text):
        self.api.update_status(twit_text)

    def search_twits(self, queries, ignore_rt=True):
        twits = []
        for query in queries:
            tweets = self.api.search(query, result_type="recent", lang="es")
            for tweet in tweets:
                if ignore_rt and tweet.text.startswith("RT"):
                    continue

                user = User.objects.get_or_create(
                    user_profile=tweet.author.screen_name
                )[0]
                twit = Tweet.objects.get_or_create(
                    tweet_id=tweet.id,
                    text=tweet.text,
                    user=user,
                )[0]

                twits.append(twit)
            time.sleep(self.sleep_time)

        return twits

    def retweet(self, tweets):
        for tweet in tweets:
            tweet.retweeted = True
            tweet.save()

            try:
                self.api.retweet(tweet.tweet_id)
                time.sleep(self.sleep_time)
            except:
                continue

    def like(self, tweets):
        for tweet in tweets:
            tweet.liked = True
            tweet.save()
            try:
                self.api.create_favorite(tweet.tweet_id)
                time.sleep(self.sleep_time)
            except:
                continue

    def unfollow(self, users):
        for user in users:
            user_profile = user.user_profile
            user.followed = False
            user.save()

            if user_profile.startswith("@"):
                user_profile = f"@{user_profile}"

            try:
                self.api.destroy_friendship(user_profile)
                time.sleep(self.sleep_time)
            except:
                continue

    def follow(self, users):
        for user in users:
            user_profile = user.user_profile
            user.followed = True
            user.save()

            if user_profile.startswith("@"):
                user_profile = f"@{user_profile}"

            try:
                self.api.create_friendship(user_profile)
                time.sleep(self.sleep_time)
            except:
                continue

    def build_queries_user_has_link(self, users, only_links=True):
        queries = []
        i = 0
        inc = 5
        while True:
            users_to_query = users[i * inc : (i + 1) * inc]
            if len(users_to_query) == 0:
                break

            i += 1
            query = self.build_query_user_has_link(users_to_query, only_links)
            queries.append(query)
        return queries

    def build_query_user_has_link(self, users, only_links=True):
        user_query = ""
        for user in users:
            user_query += f"(from:@{user.user_profile}) OR "
        user_query = (user_query + "-").replace(" OR -", "")

        links_query = "filter:links" if only_links else ""

        return f"{links_query} {user_query}"

    def build_query_with_keywords(
        self, topic, ignore_rt=True, only_links=True, lang="es"
    ):

        keywords_query = ""
        for keyword in topic.all():
            keywords_query += f"({keyword.text}) OR "
        keywords_query = (keywords_query + "-").replace(" OR -", "")

        language_query = f"(lang:{lang}) AND"
        links_query = "filter:links AND" if only_links else ""
        ignore_rt_query = "-(RT) AND" if ignore_rt else ""

        return f"{language_query} {links_query} {ignore_rt_query} ({keywords_query})"
