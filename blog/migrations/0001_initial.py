# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=140)),
                ('resume', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to=b'media/')),
                ('paragraph', models.TextField()),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('url', models.SlugField(max_length=140)),
            ],
        ),
    ]
