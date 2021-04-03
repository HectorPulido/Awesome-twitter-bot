from django.db import models


class User(models.Model):
    user_profile = models.CharField(max_length=200, unique=True, db_index=True)
    followed = models.BooleanField(default=False)
    ignore = models.BooleanField(default=False)
    must_follow = models.BooleanField(default=False)
    must_like = models.BooleanField(default=False)
    must_rt = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_profile

    def save(self, *args, **kwargs):
        self.user_profile = self.user_profile.lower()
        return super(User, self).save(*args, **kwargs)


class Tweet(models.Model):
    tweet_id = models.CharField(max_length=20, unique=True, db_index=True)
    text = models.CharField(max_length=251)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    retweeted = models.BooleanField(default=False)
    liked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Keyword(models.Model):
    text = models.CharField(max_length=50)

    def __str__(self):
        return "Keyword: " + self.text


class Topic(models.Model):
    lang = models.CharField(max_length=5)
    ignore_rt = models.BooleanField(default=False)
    only_links = models.BooleanField(default=False)
    must_like = models.BooleanField(default=False)
    must_rt = models.BooleanField(default=False)
    keywords = models.ManyToManyField(Keyword)

    def __str__(self):
        return "Keywords: " + ", ".join(
            [x[0] for x in self.keywords.values_list("text").all()]
        )
