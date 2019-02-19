from django.urls import path

from . import views
# paths : choosing a path runs a function in the views folder
urlpatterns = [
    path('', views.index, name='index'),
    path('getthegood/', views.getGood, name='getGood'),
    path('happyhappyjoyjoy/', views.happyJoy, name='happyJoy'),
]
