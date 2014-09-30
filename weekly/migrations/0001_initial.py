# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('article_content', models.TextField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('edit_date', models.DateTimeField(auto_now=True)),
                ('order', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderShip',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='排序号')),
                ('article', models.ForeignKey(to='weekly.Article', related_name='article')),
            ],
            options={
                'ordering': ('number',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Weekly',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('issues', models.CharField(max_length=500, verbose_name='刊号')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('send_date', models.DateField()),
                ('is_send', models.BooleanField(default=False)),
                ('articles', models.ManyToManyField(through='weekly.OrderShip', to='weekly.Article')),
            ],
            options={
                'ordering': ('-create_date',),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='ordership',
            name='weekly',
            field=models.ForeignKey(to='weekly.Weekly', related_name='weekly'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='weeklys',
            field=models.ManyToManyField(through='weekly.OrderShip', to='weekly.Weekly'),
            preserve_default=True,
        ),
    ]
