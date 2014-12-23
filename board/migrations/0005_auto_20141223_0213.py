# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_auto_20141223_0023'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='Password',
        ),
        migrations.AlterField(
            model_name='entry',
            name='publish',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
