# Generated by Django 3.1 on 2021-04-15 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auction_listing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction_listing',
            name='photo',
            field=models.ImageField(upload_to=''),
        ),
    ]
