# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-15 08:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0002_auto_20191015_1144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
    ]
