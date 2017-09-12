# -*- coding: utf-8 -*-
from django import forms

from .models import OrderRaise


class OrderRaiseForm(forms.ModelForm):
    class Meta:
        model = OrderRaise
        exclude = ['created_at' 'created_by']
