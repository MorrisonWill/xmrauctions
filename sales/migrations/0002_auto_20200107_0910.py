# Generated by Django 2.2.8 on 2020-01-07 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemsale',
            name='buyer_notified_of_shipment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='itemsale',
            name='seller_notified_of_payout',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='itemsale',
            name='seller_notified_of_receipt',
            field=models.BooleanField(default=False),
        ),
    ]