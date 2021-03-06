# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-23 06:40
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dragonslayer', '0049_issue_points'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('checked', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('checked_date', models.DateTimeField(blank=True, null=True)),
                ('checked_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='x', to=settings.AUTH_USER_MODEL)),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='dragonslayer.Issue')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Project')),
            ],
        ),
    ]
