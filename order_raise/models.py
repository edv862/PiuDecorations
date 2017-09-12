# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from safedelete.models import SafeDeleteModel, SOFT_DELETE_CASCADE

from client.models import Client


class OrderRaise(SafeDeleteModel):
    # Has blinds, related_name = blinds, related_query_name= blind
    _safedelete_policy = SOFT_DELETE_CASCADE

    client = models.ForeignKey(
        Client,
        related_name='orders',
        related_query_name='order'
    )

    created_at = models.DateTimeField(
        verbose_name='Fecha del levantamiento',
        auto_now_add=True
    )

    created_by = models.ForeignKey(
        User,
        verbose_name='Creado por',
        related_name='raises',
        related_query_name='raise'
    )
