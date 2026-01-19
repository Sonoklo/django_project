from django.db import models
class RestourantInfo(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=35)
    phone = models.CharField(max_length=12)
    years_decition = models.IntegerField(default=1)

class RestourantMedia(models.Model):
    restourant_img = models.ImageField(upload_to='restaurant/')
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)
    category = models.CharField(max_length=30)