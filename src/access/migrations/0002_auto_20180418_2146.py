# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-18 16:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='login_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
