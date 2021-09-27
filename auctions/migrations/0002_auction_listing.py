# Generated by Django 3.1 on 2021-04-15 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction_listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=64)),
                ('price', models.IntegerField()),
                ('des', models.CharField(max_length=256)),
                ('date', models.DateField(auto_now=True)),
                ('photo', models.ImageField(height_field=400, upload_to='photo/', width_field=300)),
            ],
        ),
    ]
