from tweepy import API
from twango.auth import get_site_auth, get_user_auth
from twango.settings import get_setting
from django.shortcuts import redirect
from django.core.exceptions import ImproperlyConfigured


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

    def process_view(self, request, view_func, view_args, view_kargs):
        """
        If this view requires twitter authorization,
        make sure this user has granted it. If not redirect
        to the twitter authorization URL.
        """
        if hasattr(view_func, 'twitter_auth_required') and \
                view_func.twitter_auth_required:
            # Make sure AuthenticationMiddlware is installed
            if not hasattr(request, 'user'):
                raise ImproperlyConfigured(
                    "TwitterMiddlware requires AuthenticationMiddleware "
                    "in order to enforce the twitter_auth_required decorator.")

            if request.user.twitter.auth is None:
                return redirect(get_setting('TWITTER_AUTH_URL'))

