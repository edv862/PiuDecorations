# -*- coding: utf-8 -*-
from django import forms

from .models import Blind


class BlindForm(forms.ModelForm):
    class Meta:
        model = Blind
        exclude = ['created_at' 'created_by']
