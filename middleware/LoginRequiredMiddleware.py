from re import compile
from django.conf import settings
from django.http import HttpResponseRedirect
from django.utils.http import is_safe_url
from django.utils.deprecation import MiddlewareMixin

EXEMPT_URLS = [compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [compile(expr) for expr in settings.LOGIN_EXEMPT_URLS]


class LoginRequiredMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if not request.user.is_authenticated():
            path = request.path_info.lstrip('/')
            if not any(m.match(path) for m in EXEMPT_URLS):
                redirect_to = settings.LOGIN_URL
                # Add 'next' GET variable to support redirection after login
                if len(path) > 0 and is_safe_url(url=request.path_info, host=request.get_host()):
                    redirect_to = "/%s?next=/%s" % (settings.LOGIN_URL, path)

                print redirect_to
                return HttpResponseRedirect(redirect_to)
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
