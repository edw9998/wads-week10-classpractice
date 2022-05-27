from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from . import views

# define url router for api.
# router = routers.DefaultRouter()
# router.register(r'Heroes', views.getData, 'Hero')

urlpatterns = [
    path('', views.getData),
    path('add/', views.addHero),
]