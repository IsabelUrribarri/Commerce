# Generated by Django 4.0.3 on 2022-10-03 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_category_auctionlist_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='watchlist',
            field=models.TextField(blank=True),
        ),
    ]
