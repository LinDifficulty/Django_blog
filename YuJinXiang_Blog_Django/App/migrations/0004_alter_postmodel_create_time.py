# Generated by Django 4.2.1 on 2023-08-02 16:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_alter_postmodel_create_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]