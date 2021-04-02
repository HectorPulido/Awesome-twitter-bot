import tweepy
import time


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
        api.update_status(tweettopublish)

    def search_twits(self, queries, ignore_rt=True):
        twits = []
        for query in queries:
            tweets = self.api.search(query, result_type="recent", lang="es")
            for tweet in tweets:
                if ignore_rt and tweet.text.startswith("RT"):
                    continue

                temp_twit = {
                    "id": tweet.id,
                    "text": tweet.text,
                    "author": tweet.author.screen_name,
                }

                twits.append(temp_twit)
            time.sleep(self.sleep_time)

        return twits

    def retweet(self, tweets):
        for tweet in tweets:
            try:
                self.api.retweet(tweet["id"])
                time.sleep(self.sleep_time)
            except:
                continue

    def like(self, tweets):
        for tweet in tweets:
            try:
                self.api.create_favorite(tweet["id"])
                time.sleep(self.sleep_time)
            except:
                continue

    def follow(self, users):
        for user in users:
            if user.startswith("@"):
                user = f"@{user}"
            try:
                self.api.create_friendship(user)
                time.sleep(self.sleep_time)
            except:
                continue

    def build_query_user_has_link(self, users, only_links=True):
        user_query = ""
        for user in users:
            user_query += f"(from:@{user}) OR "
        user_query = (user_query + "-").replace(" OR -", "")

        links_query = "filter:links" if only_links else ""

        return f"{links_query} {user_query}"

    def build_query_with_keywords(self, keywords, ignore_rt=True, only_links=True, lang="es"):
        keywords_query = ""
        for keyword in keywords:
            keywords_query += f"({keyword}) OR "
        keywords_query = (keywords_query + "-").replace(" OR -", "")

        language_query = f"(lang:{lang}) AND"
        links_query = "filter:links AND" if only_links else ""
        ignore_rt_query = "-(RT) AND" if ignore_rt else ""

        return f"{language_query} {links_query} {ignore_rt_query} ({keywords_query})"
