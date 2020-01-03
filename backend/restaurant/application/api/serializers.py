from rest_framework import serializers
from application.models import Restaurant


class RestaurantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'
