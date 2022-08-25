from rest_framework import serializers
from .models import Restaurant, Menu, Dish


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ('name',)


class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = ('restaurant', 'weekday', 'menu_dishes')


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('name', 'price')
