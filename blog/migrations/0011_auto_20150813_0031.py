# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20150813_0029'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='fecha',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='usuario',
            new_name='user',
        ),
    ]
