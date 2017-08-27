# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 08:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dbinfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_sql', models.CharField(max_length=200)),
                ('analysis_result', models.TextField()),
                ('create_time', models.TimeField(auto_now_add=True)),
                ('dbinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbinfo.DBinfo')),
            ],
        ),
    ]