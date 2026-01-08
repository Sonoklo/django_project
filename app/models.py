from django.db import models

# Create your models here.


class SiteContactInfo(models.Model):
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=50)

class BookTable(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=12)
    GUESTS = [
        ("1 Person", "1 Person"),
        ("2 People", "2 People"),
        ("3 People", "3 People"),
        ("4 People", "4 People"),
        ("+5 People", "+5 People"),
    ]
    guest_choice = models.CharField(max_length=10, choices=GUESTS) 
    date = models.DateField()
    time = models.TimeField()
    requests = models.CharField(max_length=200)
    tg_check = models.BooleanField(default=False)
class BookBusinessTable(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=12)
    GUESTS = [
        ("1 Person", "1 Person"),
        ("2 People", "2 People"),
        ("3 People", "3 People"),
        ("4 People", "4 People"),
        ("+5 People", "+5 People"),
    ]
    guest_choice = models.CharField(max_length=10, choices=GUESTS) 
    date = models.DateField()
    time = models.TimeField()
    requests = models.CharField(max_length=200)
    tg_check = models.BooleanField(default=False)
    OCCASIONS = [
        ("Birthday", "Birthday"),
        ("Anniversity", "Anniversity"),
        ("Celebration", "Celebration"),
        ("Other", "Other"),
    ]
    occasions = models.CharField(max_length=100,  choices=OCCASIONS)

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


class Dishes(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=250)
    price = models.DecimalField(decimal_places=2, max_digits=6)  
    img_link = models.ImageField(upload_to='dishes/')
    chef_choices = models.BooleanField(default=False)

class Chef_pick_dish(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=250)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    chef_dish_img = models.ImageField(upload_to='chef_dishes/')

class Category(models.Model):
    name = models.CharField(max_length=40)
    dish = models.ForeignKey(Dishes, related_name="category", on_delete=models.DO_NOTHING)
    chef_dish = models.ForeignKey(Chef_pick_dish, related_name="category",  on_delete=models.DO_NOTHING)

class Comments(models.Model):
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=150)
    nickname = models.CharField(max_length=50)
    profile_img = models.ImageField(upload_to='profile/')

class Chef_category(models.Model):
    chef_category = models.CharField(max_length=50)


class Chef(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=250)
    main_chef = models.BooleanField(default=False)
    chef_category = models.OneToOneField(Chef_category, related_name="category",  on_delete=models.DO_NOTHING)
    img_link = models.ImageField(upload_to='chefs/')

class Chef_rewards(models.Model):
    reward = models.CharField(max_length=50)
    chef = models.ForeignKey(Chef, related_name="chef_reward",  on_delete=models.DO_NOTHING)

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

class Admin(models.Model):
    user_id = models.TextField(max_length=100)
    bot_connect = models.BooleanField(default=False)

class Client_conn(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=60)
    message = models.CharField(max_length=150)

class BusinessHours(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    day = models.CharField(max_length=9, choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    closed = models.BooleanField(default=False)

class NormalHours(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    day = models.CharField(max_length=9, choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    brench = models.BooleanField(default=False)

class OperationHours(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    day = models.CharField(max_length=9, choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()

