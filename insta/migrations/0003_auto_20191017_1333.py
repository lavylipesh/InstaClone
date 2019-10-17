# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-17 10:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0002_auto_20191017_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentform',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to=settings.AUTH_USER_MODEL),
        ),
    ]
