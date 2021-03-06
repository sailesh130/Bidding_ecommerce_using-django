# Generated by Django 3.1 on 2021-04-16 02:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_auto_20210416_0733'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction_listing',
            name='user',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='lister', to='auctions.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='commenter', to='auctions.user'),
            preserve_default=False,
        ),
    ]
