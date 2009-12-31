from django.conf import settings


# Default settings for Twango.
# You may adjust them here or re-define in your
# site's setting.py file.

defaults = dict(

    # Site Twitter account credentials
        # Basic authentication
    TWITTER_SITE_USER = '',
    TWITTER_SITE_PASS = '',
        # OAuth
    TWITTER_SITE_OAUTHTOKEN = '',
    TWITTER_SITE_OAUTHSECRET = '',

    # OAuth consumer credentials
    TWITTER_CONSUMER_TOKEN = '123',
    TWITTER_CONSUMER_SECRET = '',

)


def get_setting(name):

    return getattr(settings, name, defaults[name])

