# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question_answer', '0002_question_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='test',
        ),
    ]
