# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-15 18:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_app', '0002_auto_20170915_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='name',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]