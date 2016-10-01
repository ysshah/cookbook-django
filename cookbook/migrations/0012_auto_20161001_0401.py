# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 04:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cookbook', '0011_auto_20160929_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='hello',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'hellos',
                'verbose_name': 'hello',
            },
        ),
        migrations.AlterUniqueTogether(
            name='recipe',
            unique_together=set([('user', 'name')]),
        ),
    ]