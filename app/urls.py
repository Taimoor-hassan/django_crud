from django.contrib import admin
from django.urls import path
from .views import delete, edit, home

urlpatterns = [
    path('', home, name="home"),
    path('delete/<int:id>/', delete, name="delete"),
    path('<int:id>/', edit, name="edit"),

]