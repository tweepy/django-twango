from tweepy import BasicAuthHandler, OAuthHandler
from twango.settings import get_setting


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

    # If no authentication provided, return unauthenticated API
    return API()

