from django.db import models
class Admin(models.Model):
    user_id = models.TextField(max_length=100)
    bot_connect = models.BooleanField(default=False)