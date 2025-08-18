from django.shortcuts import render

# Create your views here.
from django.conf import settings
from restaurant_management.models import restaurant_management

def homepage(request):
    restaurant = Restaurant.objects.first()

    if restaurant:
        restaurant_name = restaurant.name
    else:
        restaurant_name = settings.restaurant_name
    
    context = {"restaurant_name": restaurant_nmae}
    return render(request, "home/index.html", context)
