# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-12 15:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dragonslayer', '0045_auto_20171012_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customfield',
            name='options',
            field=models.ManyToManyField(null=True, to='dragonslayer.Option'),
        ),
    ]
