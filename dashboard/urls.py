# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import (
    DashboardMainView, DashboardLoginView,
    DashboardLogoutView
)


urlpatterns = [
    url(r'login/$', DashboardLoginView.as_view(), name='login'),
    url(r'logout/$', DashboardLogoutView.as_view(), name='logout'),

    url(r'$', DashboardMainView.as_view(), name='home'),
]