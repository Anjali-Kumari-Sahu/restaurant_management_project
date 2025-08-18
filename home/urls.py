from django.urls import path
from .views import restaurant_about

urlpatterns = [
    path("about\", restaurant_about, name="restaurant_about),
]