import json
import dropbox

from twitter_data.models import Tweet, Feature
from twitter_data.mixins import ExportCsvMixin
from django.conf import settings


def run():
    feature_config = Feature.get_feature("TWEETS_TO_DELETE")

    tweets = Tweet.objects.filter(replied=False)
    if len(tweets) < feature_config.get("count", 5000):
        return

    dbx = None
    try:
        dbx = dropbox.Dropbox(settings.ACCESS_TOKEN_DROPBOX)
        dbx.users_get_current_account()
        for entry in dbx.files_list_folder("").entries:
            print(entry.name)
    except:
        dbx = None
        print("Dropbox error, something got wrong")

    if dbx:
        file = ExportCsvMixin.export_as_csv_file(tweets)
        with open(file, "rb") as f:
            dbx.files_upload(f.read(), f"/{file}", mute=True)

    print(f"{len(tweets)} tweets deleted")
    tweets.delete()
