from django.urls import path
from .views import restaurant_about
from .import views

urlpatterns = [
    path("about\", restaurant_about, name="restaurant_about),
    path("contact/",  views.contact, name="contact"),
    
]