# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from safedelete.models import SafeDeleteModel, SOFT_DELETE_CASCADE


class Client(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    identifier = models.IntegerField(
        verbose_name=u'Identificación',
        null=True,
        blank=True
    )
    name = models.CharField(
        verbose_name=u'Nombre',
        max_length=255
    )
    direction = models.CharField(
        verbose_name=u'Dirección',
        max_length=255
    )
    email = models.EmailField(
        verbose_name=u'Correo',
    )
    phone = models.IntegerField(
        verbose_name=u'Teléfono',
    )

    created_at = models.DateTimeField(
        verbose_name=u'Fecha de creación',
        auto_now_add=True
    )

    created_by = models.ForeignKey(
        User,
        verbose_name='Creado por',
        related_name='clients',
        related_query_name='client'
    )

    def __unicode__(self):
        return "%d - %s" % (self.id, self.name)

    def __str__(self):
        return "%d - %s" % (self.id, self.name)

    def getIdentifier(self):
        return self.identifier

    def getName(self):
        return self.name

    def getEmail(self):
        return self.email

    def createdBy(self):
        return self.created_by
