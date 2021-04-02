import dropbox

from twitter_data.models import Tweet
from twitter_data.mixins import ExportCsvMixin
from django.conf import settings


def run():
    dbx = None
    try:
        dbx = dropbox.Dropbox(settings.ACCESS_TOKEN_DROPBOX)
        dbx.users_get_current_account()
        for entry in dbx.files_list_folder("").entries:
            print(entry.name)
    except:
        dbx = None
        print("Dropbox error, something got wrong")

    tweets = Tweet.objects.all()
    file = ExportCsvMixin.export_as_csv_file(tweets)

    if dbx:
        with open(file, "rb") as f:
            dbx.files_upload(f.read(), f"/{file}", mute=True)

    print(f"{len(tweets)} tweets deleted")
    tweets.delete()
