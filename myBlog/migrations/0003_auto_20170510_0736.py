# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-10 07:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myBlog', '0002_article_release_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='release_date',
            new_name='release_time',
        ),
    ]
