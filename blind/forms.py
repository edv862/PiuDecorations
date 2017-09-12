# -*- coding: utf-8 -*-
from django import forms
from django.forms import modelformset_factory

from order_raise.models import OrderRaise

from .models import Blind


class BlindForm(forms.ModelForm):
    class Meta:
        model = Blind
        exclude = ['created_at' 'created_by']


BlindOrderFormset = modelformset_factory(
    model=Blind,
    form=BlindForm,
    extra=2,
    can_delete=True
)
