from django.db import models

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
    occasions = models.CharField(max_length=100,  choices=OCCASIONS, default="Other")