from django.db import models

from food_app.models import Food
from user_app.models import Customer

class Order(models.Model):
    user = models.ForeignKey(to = Customer, on_delete=models.CASCADE)
    item = models.ForeignKey(to = Food, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}-{self.id}"