# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('question_answer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='test',
            field=models.DateTimeField(auto_now=True, default=datetime.date(2014, 11, 2)),
            preserve_default=False,
        ),
    ]
