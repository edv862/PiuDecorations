# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect


# You always have to be logged in, since LoginRequiredMiddleware requires it
# But still check just in case is user is autenticated to set up the .
class CreatedByMixin(object):
    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        self.object = form.save(commit=False)

        if self.request.user.is_authenticated():
            self.object.created_by = self.request.user
            self.object.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponse('Unauthorized', status=401)
