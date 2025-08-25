from django.urls import path
from .import views

urlpatterns = [
    path("menu/", views.menu_list, name="menu_list"),
    
]