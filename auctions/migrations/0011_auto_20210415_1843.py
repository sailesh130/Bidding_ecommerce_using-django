# Generated by Django 3.1 on 2021-04-15 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction_listing',
            name='photo',
            field=models.URLField(),
        ),
    ]