# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-04 03:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advicer', '0014_auto_20161208_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='attachment',
            field=models.FileField(upload_to='letters/%Y/%m/%d', verbose_name='File'),
        ),
    ]