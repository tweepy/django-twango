from django.db import models


class UserProfile(models.Model):
    """Twitter user profile infomation"""

    class Meta:
        abstract = True

    profile_image_url = models.URLField(verify_exists=False)
    background_image_url = models.URLField(verify_exists=False)
    background_tile = models.BooleanField()
    background_color = models.CharField(max_length=6)
    text_color = models.CharField(max_length=6)
    link_color = models.CharField(max_length=6)
    sidebar_fill_color = models.CharField(max_length=6)
    sidebar_border_color = models.CharField(max_length=6)


class User(models.Model):
    """Twitter user infomation"""

    class Meta:
        abstract = True

    twitter_id = models.PositiveIntegerField()
    name = models.CharField(max_length=20)
    screen_name = models.CharField(max_length=15)
    location = models.CharField(max_length=30)
    description = models.CharField(max_length=160)
    url = models.URLField(verify_exists=False)
    protected = models.BooleanField()
    followers_count = models.PositiveIntegerField()
    created_at = models.DateTimeField()
    favourites_count = models.PositiveIntegerField()
    utc_offset = models.IntegerField()
    time_zone = models.CharField(max_length=50)
    statuses_count = models.PositiveIntegerField()
    verified = models.BooleanField()


class Status(models.Model):
    """Twitter status"""

    class Meta:
        abstract = True

    twitter_id = models.PositiveIntegerField()
    text = models.CharField(max_length=140)
    created_at = models.DateTimeField()
    source = models.CharField(max_length=40)
    source_url = models.URLField(verify_exists=False)
    truncated = models.BooleanField()
    in_reply_to_status_id = models.PositiveIntegerField()
    in_reply_to_user_id = models.PositiveIntegerField()
    in_reply_to_screen_name = models.CharField(max_length=15)

