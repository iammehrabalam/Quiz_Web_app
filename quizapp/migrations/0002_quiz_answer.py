# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='Answer',
            field=models.IntegerField(default=b'1', verbose_name=b'Option name here 1 or 2 or 3 or 4'),
            preserve_default=True,
        ),
    ]
