from django.contrib import admin

from . import models


class TopicAdmin(admin.ModelAdmin):
    filter_horizontal = ("keywords",)


admin.site.register(models.Topic, TopicAdmin)
admin.site.register(models.Keyword)
admin.site.register(models.User)
admin.site.register(models.Tweet)
