# -*- coding: utf-8 -*-
from django import forms

from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        exclude = ['created_at', 'created_by']
        widgets = {
            'identifier': forms.NumberInput(attrs={'type': 'tel'}),
            'phone': forms.NumberInput(attrs={'type': 'tel'})
        }
