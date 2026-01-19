from django.shortcuts import render,redirect
from .models.event import *
from .models.dishes import *
from .models.admin_tg import *
from .models.book_table import *
from .models.site import *
from .models.restourant import *
from .models.chef import *
from .models.hours import *
from .models.category import *
from .models.comments import *
from .models.client_conn import *
from .forms.client_conn import *
from .forms.book_table import *
from django.contrib import messages

# Create your views here.
def main(request):
    form_book_table = BookTableForm()
    form_book_bussiness_table = BookBusinessTableForm()
    form_client_conn = ClientConnForm()

    site_info = SiteContactInfo.objects.first()
    restourant_info = RestourantInfo.objects.first()
    dishes = Dishes.objects.all()
    categorys = Category.objects.all()
    chefs = Chef.objects.all()
    event = Event.objects.first()
    special_events = SpecialEvents.objects.all()
    comments = Comments.objects.all()
    chef_picks = Chef_pick_dish.objects.all()
    event_categories = EventCategory.objects.filter(spec_event__in=special_events)
    restourant_medias = RestourantMedia.objects.all()
    bis_hours = BusinessHours.objects.all()
    normal_hours = NormalHours.objects.all()
    oper_hours = OperationHours.objects.all()
    context = {"site_info": site_info, "restourant_info": restourant_info,"dishes": dishes, "categorys": categorys,
                "chefs": chefs, "event": event,"special_events": special_events,
                "testimonials": comments,"form_book_table": form_book_table,"form_book_bussiness": form_book_bussiness_table,
                "chef_picks": chef_picks, "form_client_conn": form_client_conn, "event_categories":event_categories, 
                "restourant_medias": restourant_medias, "bis_hours": bis_hours, "normal_hours": normal_hours, "oper_hours":oper_hours }

    return render(request, "index.html", context=context)

def book_table_create(request):
    if request.method == "POST":
        form_book_table = BookTableForm(request.POST)
        if form_book_table.is_valid():
            form_book_table.save()
        else:
            messages.error(request, "Fail by booking table")
    return redirect("/")

def book_bussiness_table_create(request):
    if request.method == "POST":
        form_book_bussiness_table = BookBusinessTableForm(request.POST)
        if form_book_bussiness_table.is_valid():
            form_book_bussiness_table.save()
        else:    
            messages.error(request, "Fail by booking bussiness table")
    return redirect("/")

def client_connection_create(request):
    if request.method == "POST":
        form_client_conn = ClientConnForm(request.POST)
        if form_client_conn.is_valid():
            form_client_conn.save()
        else: 
            messages.error(request, "Fail by sending message ")
    return redirect("/")