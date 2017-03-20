# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aabrl', '0002_auto_20170319_0222'),
    ]

    operations = [
        migrations.CreateModel(
            name='usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=20)),
                ('sobrenome', models.CharField(max_length=20)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('data_criacao', models.DateTimeField(auto_now=True, verbose_name='Data Criação')),
            ],
            options={
                'verbose_name_plural': ['nomes'],
                'verbose_name': ['nome'],
                'ordering': ['data_criacao'],
            },
        ),
    ]
