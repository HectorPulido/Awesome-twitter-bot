from django.contrib import admin

from .models import Topic, Keyword, User, Tweet
from .mixins import ExportCsvMixin


class TopicAdmin(admin.ModelAdmin):
    filter_horizontal = ("keywords",)


class TweetsAdmin(admin.ModelAdmin, ExportCsvMixin):
    actions = ["export_as_csv_response"]


admin.site.register(Topic, TopicAdmin)
admin.site.register(Keyword)
admin.site.register(User)
admin.site.register(Tweet, TweetsAdmin)
