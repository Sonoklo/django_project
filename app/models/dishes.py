from django.db import models
class Dishes(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=250)
    price = models.DecimalField(decimal_places=2, max_digits=6)  
    img_link = models.ImageField(upload_to='dishes/')
    chef_choices = models.BooleanField(default=False)