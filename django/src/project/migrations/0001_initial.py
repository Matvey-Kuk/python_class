# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-28 01:08
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('mark', models.CharField(default='color:red', max_length=20)),
            ],
        ),
    ]
