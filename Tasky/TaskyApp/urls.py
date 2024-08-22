from django.urls import path
from django.forms import *
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('view', views.view, name="view" ),
    path('add', views.add, name="add")
]