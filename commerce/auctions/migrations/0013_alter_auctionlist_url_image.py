# Generated by Django 4.0.3 on 2022-10-03 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_alter_user_watchlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlist',
            name='url_image',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
