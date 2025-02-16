from django.db import models
from choices import Choices
from django.core.validators import MinValueValidator


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField()
    directions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(choices=Choices.FOOD_TYPES, default='veg')
    minutes_taken = models.IntegerField(validators=[
        MinValueValidator(1),
    ])
    image = models.ImageField(upload_to='images/', blank=True, null=True)
