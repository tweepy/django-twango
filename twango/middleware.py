from tweepy import API
from twango.auth import get_site_auth


class TwitterMiddleware(object):

    def __init__(self):
        self._site_api = API(get_site_auth())

    def process_request(self, request):
        """Add the site twitter API object"""
        request.twitter = self._site_api

