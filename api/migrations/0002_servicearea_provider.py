# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicearea',
            name='provider',
            field=models.ForeignKey(related_name='service_area', default=None, to='api.Provider'),
        ),
    ]
