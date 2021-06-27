from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add_record', views.add_record, name="add_record"),
    path('add_record_action', views.add_record_action, name="add_record_action"),
    path('show_records', views.show_records, name="show_records"),
    path('delete_data', views.delete_data, name="delete_data"),
]