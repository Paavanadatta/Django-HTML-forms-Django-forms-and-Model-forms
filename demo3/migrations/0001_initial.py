# Generated by Django 4.0.4 on 2022-04-30 11:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='enqmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('desc', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime(2022, 4, 30, 17, 11, 38, 122062))),
            ],
        ),
    ]