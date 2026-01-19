from django.db import models
from .dishes import Dishes
from .chef import Chef_pick_dish
class Category(models.Model):
    name = models.CharField(max_length=40)
    dish = models.ForeignKey(Dishes, related_name="category", on_delete=models.DO_NOTHING)
    chef_dish = models.ForeignKey(Chef_pick_dish, related_name="category",  on_delete=models.DO_NOTHING)