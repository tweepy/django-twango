def twitter_auth_required(view_func):
    """
    Decorator for views that requires the authenicated
    user to have authorized the site on Twitter. If no
    credentials are on record, user will be directed to
    a page to authorize the site.
    """

    view_func.twitter_auth_required = True
    return view_func

