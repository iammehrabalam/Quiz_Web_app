# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='quiz',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Type', models.CharField(blank=True, max_length=20, choices=[(b'Easy', b'Easy'), (b'Medium', b'Medium'), (b'Difficult', b'Difficult')])),
                ('Question', models.CharField(max_length=300)),
                ('Option1', models.CharField(max_length=100)),
                ('Option2', models.CharField(max_length=100)),
                ('Option3', models.CharField(max_length=100)),
                ('Option4', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=500)),
                ('Displaytime', models.IntegerField()),
                ('Position', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
