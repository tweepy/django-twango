from django.http import HttpResponse
from twango.decorators import twitter_auth_required


@twitter_auth_required
def test(request):

    return HttpResponse('works!')

