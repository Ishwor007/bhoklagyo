from django.db import models

from restaurant_app.models import Restaurant
from user_app.models import Customer


class Food(models.Model):
    name = models.CharField(max_length=255,)
    unit_price = models.FloatField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Rating(models.Model):
    user = models.ForeignKey(to=Customer, on_delete=models.DO_NOTHING)
    food = models.ForeignKey(to=Food, on_delete=models.DO_NOTHING)
    rate = models.SmallIntegerField()
    rate_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.food}-{self.id}"

    