# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy

from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView


class DashboardLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('dashboard:home')


class DashboardLogoutView(LoginView):
    success_url = reverse_lazy('dashboard:home')


class DashboardMainView(TemplateView):
    template_name = 'home.html'