# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-01-17 06:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('podopieczni', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='podopieczny',
            old_name='desciption',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='podopieczny',
            old_name='desciption_html',
            new_name='description_html',
        ),
    ]