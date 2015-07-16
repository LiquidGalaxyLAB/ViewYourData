# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kmls_management', '0002_auto_20150713_1043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kml',
            name='url',
        ),
    ]
