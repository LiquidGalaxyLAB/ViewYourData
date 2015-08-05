# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kmls_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kml',
            name='file',
            field=models.FileField(default=None, upload_to=b'.'),
            preserve_default=False,
        ),
    ]
