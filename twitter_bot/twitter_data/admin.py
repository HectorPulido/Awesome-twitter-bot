from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Topic, Keyword, User, Tweet
from .mixins import ExportCsvMixin


class TopicsAdmin(admin.ModelAdmin):
    filter_horizontal = ("keywords",)


class TweetsAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ("text", "user", "retweeted", "liked", "go_to_tweet")
    list_filter = (
        "retweeted",
        "liked",
    )
    search_fields = ["user__user_profile", "text"]
    actions = ["export_as_csv_response"]

    def go_to_tweet(self, obj):
        link = f"https://twitter.com/{obj.user.user_profile}/status/{obj.id}"
        return mark_safe(f'<a href="{link}" target="blank">link</a>')


class UsersAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = (
        "user_profile",
        "followed",
        "ignore",
        "must_follow",
        "must_like",
        "must_rt",
        "go_to_profile",
    )
    list_editable = (
        "ignore",
        "must_follow",
        "must_like",
        "must_rt",
    )
    list_filter = (
        "ignore",
        "must_follow",
        "must_like",
        "must_rt",
    )
    search_fields = ["user_profile"]

    def go_to_profile(self, obj):
        link = f"https://twitter.com/{obj.user_profile}"
        return mark_safe(f'<a href="{link}" target="blank">link</a>')


admin.site.register(Topic, TopicsAdmin)
admin.site.register(Keyword)
admin.site.register(User, UsersAdmin)
admin.site.register(Tweet, TweetsAdmin)
