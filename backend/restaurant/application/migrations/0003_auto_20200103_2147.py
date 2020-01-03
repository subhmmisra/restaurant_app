# Generated by Django 2.2.6 on 2020-01-03 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_restaurant_res_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='aggregate_rating',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='rating_color',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='rating_text',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='votes',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
