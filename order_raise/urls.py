# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import (
    OrderRaiseCreateView
)


urlpatterns = [
    url(r'create/$', OrderRaiseCreateView.as_view(), name='create'),
]