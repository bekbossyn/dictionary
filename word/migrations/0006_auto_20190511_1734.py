# Generated by Django 2.2.1 on 2019-05-11 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0005_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='language',
            name='name',
        ),
        migrations.AddField(
            model_name='language',
            name='code_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='language',
            name='display_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
