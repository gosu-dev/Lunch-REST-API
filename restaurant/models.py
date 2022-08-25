from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Dish(models.Model):
    price = models.FloatField()
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'Name: {self.name}. Price: {self.price}'


class Menu(models.Model):
    weekday = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(7)])
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    menu_dishes = models.ManyToManyField(Dish, related_name='menus')

    class Meta:
        unique_together = ('weekday', 'restaurant',)
