# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 15:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trello_app', '0005_auto_20170403_1540'),
    ]

    operations = [
        migrations.RenameField(
            model_name='board',
            old_name='users',
            new_name='user',
        ),
    ]
