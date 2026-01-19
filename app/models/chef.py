from django.db import models
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
class Chef_pick_dish(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=250)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    chef_dish_img = models.ImageField(upload_to='chef_dishes/')