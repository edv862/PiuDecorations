# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models
from safedelete.models import SafeDeleteModel, SOFT_DELETE_CASCADE


class Blind(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    INSTALLATION_TYPES = (
        (0, 'Techo'),
        (1, 'Pared'),
    )

    PIPE_TYPES = (
        (0, '38mm'),
        (1, '45mm'),
        (2, '70mm'),
    )

    WEIGHT_TYPE = (
        (0, 'Chato'),
        (1, 'Redondo'),
    )

    CONTROL_TYPE = (
        (0, 'Derecha'),
        (1, 'Izquierda'),
    )

    frame_height = models.FloatField(
        verbose_name='Alto de marco',

    )
    frame_width = models.FloatField(
        verbose_name='Ancho de marco',
    )

    finished_height = models.FloatField(
        verbose_name='Alto terminado',
    )
    finished_width = models.FloatField(
        verbose_name='Ancho terminado',
    )

    installation = models.CharField(
        verbose_name=u'Instalación',
        choices=INSTALLATION_TYPES,
        max_length=50
    )

    pipe = models.CharField(
        verbose_name='Tubo',
        choices=PIPE_TYPES,
        max_length=50
    )

    weight = models.CharField(
        verbose_name='Peso',
        choices=WEIGHT_TYPE,
        max_length=50
    )

    control = models.CharField(
        verbose_name='Mando',
        choices=CONTROL_TYPE,
        max_length=50
    )

    type = models.CharField(
        verbose_name='Tipo de persiana',
        max_length=500,
        blank=True
    )

    fabric = models.CharField(
        verbose_name=u'Código de tela',
        max_length=500,
        blank=True
    )

    comment = models.CharField(
        verbose_name=u'Comentarios',
        max_length=1000,
        blank=True
    )

    created_at = models.DateTimeField(
        verbose_name=u'Fecha de creación',
        auto_now_add=True
    )

    created_by = models.ForeignKey(
        User,
        verbose_name='Creado por',
        related_name='blids',
        related_query_name='blind'
    )
