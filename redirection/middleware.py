from .models import Redirection
from django.shortcuts import redirect


class RedirectionBasedOnSlug(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            redirection_object = Redirection.objects.get(original_url=request.build_absolute_uri())
            if redirection_object is None:
                return redirect(request.build_absolute_uri())
            else:
                return redirect(redirection_object.redirection_to)
        except Exception:
            pass
        return self.get_response(request)
