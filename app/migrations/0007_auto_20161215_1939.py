# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-15 19:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20161215_1820'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'კომენტარი', 'verbose_name_plural': 'კომენტარები'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'პოსტი', 'verbose_name_plural': 'პოსტები'},
        ),
    ]