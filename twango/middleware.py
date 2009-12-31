from tweepy import API
from twango.auth import get_site_auth, get_user_auth


class TwitterMiddleware(object):

    def __init__(self):
        self._site_api = API(get_site_auth())

    def process_request(self, request):
        """Add the site twitter API object"""
        request.twitter = self._site_api

        """Add the user twitter API object if auth
            middleware is activated."""
        if hasattr(request, 'user'):
            request.user.twitter = API(get_user_auth(request.user))

