from django.db import models

class SiteContactInfo(models.Model):
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=50)