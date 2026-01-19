from django.db import models
class Event(models.Model):
    name = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField()
    event_img_link = models.ImageField(upload_to='events/')  

class SpecialEvents(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=250)
    img_link = models.ImageField(upload_to="SpecialEvent/")
class EventCategory(models.Model):
    name = models.CharField(max_length=50)
    spec_event = models.ForeignKey(SpecialEvents, related_name="event_category",  on_delete=models.DO_NOTHING)