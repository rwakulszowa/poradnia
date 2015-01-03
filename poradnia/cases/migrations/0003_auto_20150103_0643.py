# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0002_auto_20150102_1532'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='case',
            options={'permissions': (('can_select_client', 'Can select client'), ('can_view_all', 'Can view all cases'), ('can_view_free', 'Can view free'))},
        ),
    ]
