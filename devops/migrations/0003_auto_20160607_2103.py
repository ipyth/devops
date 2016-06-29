# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-07 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devops', '0002_auto_20160607_1738'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='host',
            name='note',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='host',
            name='os',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='host',
            name='services',
            field=models.ManyToManyField(to='devops.Services'),
        ),
    ]