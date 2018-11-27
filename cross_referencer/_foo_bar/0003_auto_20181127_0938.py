# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-11-27 09:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cross_referencer', '0002_auto_20181127_0230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crossreference',
            name='destination',
        ),
        migrations.AddField(
            model_name='crossreference',
            name='destination',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='destination', to='cross_referencer.BiblePassage'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='crossreference',
            name='start',
        ),
        migrations.AddField(
            model_name='crossreference',
            name='start',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='start', to='cross_referencer.BiblePassage'),
            preserve_default=False,
        ),
    ]