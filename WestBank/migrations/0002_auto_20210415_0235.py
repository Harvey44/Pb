# Generated by Django 2.2.6 on 2021-04-15 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WestBank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customprofile',
            name='balance',
            field=models.CharField(max_length=2000),
        ),
    ]
