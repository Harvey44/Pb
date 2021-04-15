from django.conf.urls import url
from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', views.index, name="index"),
    path('account/app', views.home, name="home"),
    path('account/app', views.home, name="home"),
    path('account/send', views.send, name="send"),
    path('account/history', views.transfers, name="history"),
    path('account/profile', views.profile, name="profile"),
    path('account/postpin', views.post_pin, name="postpin"),
    path('account/postcode', views.post_code, name="postcode"),
    path('account/postransfer', views.post_transfer, name="posttransfer"),




]
