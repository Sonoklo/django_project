from django.db import models

class Client_conn(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=60)
    message = models.CharField(max_length=150)