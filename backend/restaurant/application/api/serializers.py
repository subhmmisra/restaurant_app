from rest_framework import serializers
from application.models import Restaurant

'''serializers'''


class RestaurantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'
