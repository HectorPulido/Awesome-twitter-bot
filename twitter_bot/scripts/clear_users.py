import json
import dropbox

from twitter_data.models import User, Feature
from twitter_data.mixins import ExportCsvMixin
from django.conf import settings


def run():
    feature_config = json.loads(Feature.objects.get(name="USERS_TO_DELETE").value)

    users = User.objects.filter(
        followed=False,
        ignore=False,
        must_follow=False,
        must_like=False,
        must_rt=False,
        retweet_count__lte=feature_config.get("min_retweets", 5),
    )

    if len(users) < feature_config.get("count", 5000):
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
        file = ExportCsvMixin.export_as_csv_file(users)
        with open(file, "rb") as f:
            dbx.files_upload(f.read(), f"/{file}", mute=True)

    print(f"{len(users)} users deleted")
    users.delete()
