# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-15 17:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20161212_0805'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name_plural': 'კომენტარები'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name_plural': 'პოსტები'},
        ),
    ]
