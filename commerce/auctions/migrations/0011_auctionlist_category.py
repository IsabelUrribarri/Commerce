# Generated by Django 4.0.3 on 2022-09-23 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_user_watchlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlist',
            name='category',
            field=models.CharField(default='None', max_length=40),
            preserve_default=False,
        ),
    ]
