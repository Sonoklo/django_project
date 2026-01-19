from django.db import models
class Comments(models.Model):
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=150)
    nickname = models.CharField(max_length=50)
    profile_img = models.ImageField(upload_to='profile/')