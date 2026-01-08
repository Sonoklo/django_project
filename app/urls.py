from django.urls import path
from app import views
from django.conf.urls.static import static
from project.settings import MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    path('', views.main, name="main"),
    path('book-table-create/', views.book_table_create, name='book_create'),
    path('book-bussiness-table-create/', views.book_bussiness_table_create, name='book_bis_create'),
    path('client-connection-create/', views.client_connection_create, name='client_conn')
] + static(MEDIA_URL, document_root=MEDIA_ROOT)