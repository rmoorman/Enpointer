# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-08 00:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dragonslayer', '0004_auto_20170907_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='priority',
            field=models.CharField(blank=True, default='mid', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='issue',
            name='status',
            field=models.CharField(blank=True, default='open', max_length=100, null=True),
        ),
    ]
