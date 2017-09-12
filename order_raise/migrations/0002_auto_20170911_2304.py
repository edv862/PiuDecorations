# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-11 23:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order_raise', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderraise',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', related_query_name='order', to='client.Client'),
        ),
    ]
