# Generated by Django 2.2.6 on 2021-04-15 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WestBank', '0004_auto_20210415_0732'),
    ]

    operations = [
        migrations.AddField(
            model_name='customprofile',
            name='figure',
            field=models.IntegerField(default=0),
        ),
    ]