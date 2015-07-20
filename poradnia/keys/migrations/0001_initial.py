# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import keys.utils


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(default=keys.utils.make_random_password, max_length=75, verbose_name='Key')),
                ('description', models.CharField(max_length=75, verbose_name='Description')),
                ('created_on', models.DateField(auto_now_add=True, verbose_name='Created on')),
                ('used_on', models.DateField(null=True, verbose_name='Used on')),
                ('download_on', models.DateField(null=True, verbose_name='Download on')),
                ('user', models.ForeignKey(verbose_name='User', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Access key',
                'verbose_name_plural': 'Access keys',
            },
            bases=(models.Model,),
        ),
    ]