# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-04 01:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='last_updated',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Time to get the last value'),
        ),
    ]
