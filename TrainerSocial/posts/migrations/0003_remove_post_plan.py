# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-01-18 00:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20210118_0054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='plan',
        ),
    ]