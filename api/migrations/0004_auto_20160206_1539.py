# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20160206_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='email',
            field=models.EmailField(unique=True, max_length=254),
        ),
    ]
