# Generated by Django 2.2.8 on 2020-01-10 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='whereabouts',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
