# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150803_1753'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='paragraph',
            new_name='content',
        ),
        migrations.AlterField(
            model_name='blog',
            name='usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
