# Generated by Django 2.2.1 on 2019-05-11 06:44

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0003_auto_20190511_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict),
        ),
    ]
