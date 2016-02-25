# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_servicearea_provider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='user',
            field=models.OneToOneField(related_name='provider', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='servicearea',
            name='provider',
            field=models.ForeignKey(related_name='service_area', to='api.Provider'),
        ),
    ]
