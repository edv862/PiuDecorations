# -*- coding: utf-8 -*-
from django.conf.urls import url, include

from .views import (
    ClientCreateView, ClientListView,
    ClientUpdateView, ClientDeleteView
)


urlpatterns = [
    url(r'create/$', ClientCreateView.as_view(), name='create'),
    url(r'update/(?P<pk>[0-9]*)/$', ClientUpdateView.as_view(), name='edit'),
    url(r'delete/(?P<pk>[0-9]*)/$', ClientDeleteView.as_view(), name='delete'),
    url(r'$', ClientListView.as_view(), name='list'),
]
