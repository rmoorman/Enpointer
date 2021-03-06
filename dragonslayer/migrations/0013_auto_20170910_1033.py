# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-10 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dragonslayer', '0012_auto_20170909_1323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='issue',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='project',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='orgs',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='projects',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='sections',
        ),
        migrations.AddField(
            model_name='issue',
            name='comments',
            field=models.ManyToManyField(to='dragonslayer.Comment'),
        ),
        migrations.AddField(
            model_name='org',
            name='sections',
            field=models.ManyToManyField(to='dragonslayer.Section'),
        ),
        migrations.AddField(
            model_name='project',
            name='issues',
            field=models.ManyToManyField(to='dragonslayer.Issue'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='org',
            field=models.ManyToManyField(to='dragonslayer.Org'),
        ),
    ]
