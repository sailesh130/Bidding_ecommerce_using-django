# Generated by Django 3.1 on 2021-04-15 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_auto_20210415_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction_listing',
            name='photo',
            field=models.URLField(max_length=520),
        ),
    ]
