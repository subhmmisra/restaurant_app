# Generated by Django 2.2.6 on 2020-01-03 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_restaurant_cuisines'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='has_booking',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='has_online_delivery',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]