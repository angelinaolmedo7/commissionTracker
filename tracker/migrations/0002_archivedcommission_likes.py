# Generated by Django 2.2.6 on 2019-12-13 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='archivedcommission',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]