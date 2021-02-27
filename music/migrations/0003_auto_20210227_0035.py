# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20180214_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(max_length=10, default='Male', choices=[('Male', 'Male'), ('Female', 'Female')]),
        ),
        migrations.AlterField(
            model_name='song',
            name='genre',
            field=models.CharField(max_length=25, default='Pop', choices=[('Pop', 'Pop'), ('Reggae', 'Reggae'), ('Country', 'Country'), ('Jazz', 'Jazz'), ('Hip Hop', 'Hip Hop'), ('Rock', 'Rock'), ('R&B and Souls', 'R&B and Souls'), ('Dangdut', 'Dangdut')]),
        ),
    ]
