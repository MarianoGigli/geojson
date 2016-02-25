# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20160206_1539'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicearea',
            old_name='polygon',
            new_name='area',
        ),
    ]
