# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20150811_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='usuario',
            field=models.ForeignKey(related_name='blog', to=settings.AUTH_USER_MODEL),
        ),
    ]
