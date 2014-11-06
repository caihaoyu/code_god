# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question_answer', '0003_remove_question_test'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='question',
            index_together=set([('title',)]),
        ),
        migrations.AlterIndexTogether(
            name='tag',
            index_together=set([('title',)]),
        ),
    ]
