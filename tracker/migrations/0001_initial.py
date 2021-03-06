# Generated by Django 2.2.6 on 2019-12-09 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArchivedCommission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commission_title', models.CharField(max_length=50)),
                ('commissioner_name', models.CharField(max_length=50)),
                ('commissioner_platform', models.CharField(max_length=50)),
                ('commission_description', models.CharField(max_length=1000)),
                ('creation_date', models.DateTimeField()),
                ('completion_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Commission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commission_title', models.CharField(max_length=50)),
                ('commissioner_name', models.CharField(max_length=50)),
                ('commissioner_platform', models.CharField(max_length=50)),
                ('commission_description', models.CharField(max_length=1000)),
                ('complexity_rating', models.IntegerField(default=0)),
                ('creation_date', models.DateTimeField()),
            ],
        ),
    ]
