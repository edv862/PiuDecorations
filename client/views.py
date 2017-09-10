# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView

from mixin.createdbymixin import CreatedByMixin

from .models import Client
from .forms import ClientForm


class ClientCreateView(CreatedByMixin, CreateView):
    context_object_name = 'client'
    form_class = ClientForm
    model = Client
    queryset = Client.objects.all()
    template_name = 'client-create.html'
    success_url = reverse_lazy('client:list')


class ClientListView(ListView):
    context_object_name = 'clients'
    model = Client
    queryset = Client.objects.all()
    template_name = 'client-list.html'


class ClientUpdateView(UpdateView):
    context_object_name = 'client'
    form_class = ClientForm
    model = Client
    queryset = Client.objects.all()
    template_name = 'client-edit.html'
    success_url = reverse_lazy('client:list')


class ClientDeleteView(DeleteView):
    model = Client
    queryset = Client.objects.all()
    success_url = reverse_lazy('client:list')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return self.delete(request, *args, **kwargs)
