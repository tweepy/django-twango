from tweepy import BasicAuthHandler, OAuthHandler
from twango.settings import get_setting
from twango.models import UserCredentials


def get_consumer_creds():
    """Return consumer OAuth credentials"""
    return get_setting('TWITTER_CONSUMER_TOKEN'), \
            get_setting('TWITTER_CONSUMER_SECRET')


def get_site_auth():
    """Return auth handler for site API object"""

    # First check for basic auth credentials
    twitter_user = get_setting('TWITTER_SITE_USER')
    twitter_pass = get_setting('TWITTER_SITE_PASS')
    if twitter_user and twitter_pass:
        return BasicAuthHandler(twitter_user, twitter_pass)

    # If no basic, check for OAuth
    consumer_token, consumer_secret = get_consumer_creds()
    oauth_token = get_setting('TWITTER_SITE_OAUTHTOKEN')
    oauth_secret = get_setting('TWITTER_SITE_OAUTHSECRET')
    if consumer_token and consumer_secret and oauth_token and oauth_secret:
        auth = OAuthHandler(consumer_token, consumer_secret)
        auth.set_access_token(oauth_token, oauth_secret)
        return auth


def get_user_auth(user):
    """Return auth handler for user API object"""

    if user.is_authenticated() is False:
        return

    # Fetch the user's twitter credentials from DB
    try:
        creds = UserCredentials.objects.get(user=user)
    except UserCredentials.DoesNotExist:
        return

    # Do we have basic credentials?
    if creds.username and creds.password:
        return BasicAuthHandler(creds.username, creds.password)

    # How about OAuth?
    consumer_creds = get_consumer_creds()
    if consumer_creds and creds.oauth_token and creds.oauth_secret:
        auth = OAuthHandler(*consumer_creds)
        auth.set_access_token(creds.oauth_token, creds.oauth_secret)
        return auth

