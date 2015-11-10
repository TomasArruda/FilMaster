# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('birthday', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('director_name', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('productor_name', models.CharField(max_length=100)),
                ('grade', models.FloatField()),
                ('artists', models.ManyToManyField(to='analyser.Artist')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
