from django.db import models

# Create your models here.


class Restaurant(models.Model):
    res_id = models.IntegerField(null=True, blank=True)
    res_name = models.CharField(blank=True, null=True, max_length=50)
    avg_cost_two = models.IntegerField(null=True, blank=True)
    cuisines = models.CharField(blank=True, null=True, max_length=50)
    curreny = models.CharField(null=True, blank=True, max_length=50)
    has_booking = models.CharField(null=True, blank=True, max_length=50)
    has_online_delivery = models.CharField(
        null=True, blank=True, max_length=50)
    aggregate_rating = models.FloatField(null=True, blank=True)
    rating_color = models.CharField(null=True, blank=True, max_length=50)
    rating_text = models.CharField(null=True, blank=True, max_length=50)
    votes = models.CharField(null=True, blank=True, max_length=50)

    def __str__(self):
        return self.res_name
