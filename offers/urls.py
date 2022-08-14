from django.urls import path
from . import views

app_name = 'offers'

urlpatterns = [
  path('normal', views.normal_offers, name='offers'),
]