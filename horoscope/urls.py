from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:sing_zodiac>', views.get_info_about_sing_zodiac_by_number),
    path('<str:sing_zodiac>', views.get_info_about_sing_zodiac, name='horoscope-name'),
]
