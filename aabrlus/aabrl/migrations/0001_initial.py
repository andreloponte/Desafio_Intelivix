# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Urls',
            fields=[
                ('encurtamento_id', models.SlugField(primary_key=True, serialize=False, max_length=6)),
                ('url_original', models.URLField()),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('contador', models.IntegerField(default=0)),
            ],
        ),
    ]
