# Generated by Django 3.1 on 2021-04-16 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20210416_1017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='user',
        ),
    ]