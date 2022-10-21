from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating as StarRating
from restaurant_app.models import Restaurant
from user_app.models import Customer


class Food(models.Model):
    name = models.CharField(max_length=255,)
    image = models.ImageField(upload_to='images', blank=True)
    image_url = models.URLField(blank=True)
    unit_price = models.FloatField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, null=True)
    ratings = GenericRelation(StarRating, related_query_name='foods')

    class Meta:
        db_table = 'food'

    def __str__(self):
        return self.name

# class Rating(models.Model):
#     user = models.ForeignKey(to=Customer, on_delete=models.DO_NOTHING)
#     food = models.ForeignKey(to=Food, on_delete=models.DO_NOTHING)
#     ratings = GenericRelation(StarRating, related_query_name='rating')
#     rate_on = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.food}-{self.id}"

#     class Meta:
#         db_table = 'rating'