# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-05-20 02:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0019_add_custom_slots'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='time_accepted_tos',
            field=models.DateTimeField(null=True),
        ),
    ]