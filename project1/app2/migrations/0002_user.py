# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama_depan', models.CharField(max_length=128)),
                ('nama_belakang', models.CharField(max_length=128)),
                ('email', models.EmailField(unique=True, max_length=264)),
            ],
        ),
    ]
