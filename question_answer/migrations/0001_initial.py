# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('content', models.TextField(verbose_name='内容')),
                ('is_accept', models.BooleanField(verbose_name='是否被采纳', default=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('edit_date', models.DateTimeField(auto_now=True)),
                ('original_author', models.CharField(verbose_name='原作者', null=True, max_length=100)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Evaluate',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('ip', models.CharField(max_length=100)),
                ('approval', models.BooleanField(verbose_name='是否赞同', default=False)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='KeyWord',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('word', models.CharField(verbose_name='关键词', max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(verbose_name='标题', db_index=True, max_length=100)),
                ('content', models.TextField(verbose_name='内容')),
                ('trackback_url', models.CharField(verbose_name='引用地址', max_length=300)),
                ('original_author', models.CharField(verbose_name='原作者', null=True, max_length=100)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('edit_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=30)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('edit_date', models.DateTimeField(auto_now=True)),
                ('questions', models.ManyToManyField(to='question_answer.Question')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='keyword',
            name='question',
            field=models.ForeignKey(verbose_name='问题', to='question_answer.Question'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='questions',
            field=models.ForeignKey(verbose_name='问题', to='question_answer.Question'),
            preserve_default=True,
        ),
    ]
