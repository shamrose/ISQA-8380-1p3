# Generated by Django 2.0.5 on 2018-09-24 00:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_auto_20180923_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 24, 0, 30, 24, 285365, tzinfo=utc)),
        ),
    ]
