from secret import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
from clases import TwitterBot

users = [
    "hector_pulido_",
    "puni_xa",
    "DogedevCD",
    "Luis_LiraC",
    "gndx",
    "HeyNauGames",
    "l_draven",
    "OgrePixel",
    "SteveOgre",
    "sen_mald",
]

bot = TwitterBot(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, 5)

queries_to_retweet_and_like = [bot.build_query_user_has_link(users)]

queries_to_retweet = [
    bot.build_query_with_keywords(
        ["gamedev", "desarrollo de videojuegos", "#gamedev", "indie game"]
    ),
    bot.build_query_with_keywords(
        ["machine learning", "data science", "inteligencia artificial"]
    ),
]

bot.follow(users)

# twits = bot.search_twits(queries)
# bot.retweet(twits)
import ipdb

ipdb.set_trace()
