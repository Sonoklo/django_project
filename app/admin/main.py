from django.contrib import admin
from app.models.event import *
from app.models.dishes import *
from app.models.admin_tg import *
from app.models.book_table import *
from app.models.site import *
from app.models.restourant import *
from app.models.chef import *
from app.models.hours import *
from app.models.category import *
# Register your models here.

admin.site.register((SiteContactInfo, RestourantInfo,  Admin, Chef_category, Chef_rewards, EventCategory, SpecialEvents, RestourantMedia, Category, BusinessHours, OperationHours, NormalHours),)