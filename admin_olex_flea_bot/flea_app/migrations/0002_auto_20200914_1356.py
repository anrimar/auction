# Generated by Django 3.1.1 on 2020-09-14 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flea_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='external_id',
            field=models.PositiveIntegerField(null=True, verbose_name='ID сообщения в Барахолке'),
        ),
    ]
