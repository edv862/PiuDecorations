# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, UpdateView,
    ListView, DeleteView,
    FormView, View
)

from blind.forms import BlindOrderFormset
from client.forms import ClientForm

from .models import OrderRaise
from .forms import OrderRaiseForm


class OrderRaiseCreateView(CreateView):
    template_name = 'order-raise-create.html'
    models = OrderRaise
    queryset = OrderRaise.objects.all()
    form_class = OrderRaiseForm
    success_url = reverse_lazy('dashboard:home')

    def get_context_data(self, **kwargs):
        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()

        context = super(OrderRaiseCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['client_form'] = ClientForm(self.request.POST)
            context['blinds_formset'] = BlindOrderFormset(self.request.POST)
        else:
            context['client_form'] = ClientForm()
            context['blinds_formset'] = BlindOrderFormset()
        return context

    def form_valid(self, form):
        context = self.get_context_data()

        client = context['client_form']
        blinds = context['blinds_formset']

        # Save new client.
        client.save()
        blinds.save()

        return super(OrderRaiseCreateView, self).form_valid(form)
