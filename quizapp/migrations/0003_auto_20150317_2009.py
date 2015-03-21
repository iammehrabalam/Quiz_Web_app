# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0002_quiz_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='Answer',
            field=models.IntegerField(default=b'1', verbose_name=b'Answer ( Type Which option )'),
            preserve_default=True,
        ),
    ]
