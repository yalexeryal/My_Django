from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('<int:sing_days>', views.get_info_about_sing_days_by_number),
    path('<str:sing_days>', views.get_info_about_sing_days, name='days-name'),
]

