import requests
from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.shortcuts import render
from restaurant_management.models import restaurant_management


def home(request):
    response = requests.get("http://127.0.0.1:8000/api/menu/")
    menu_items = response.json()  if response.status_code == 200 else []
    return render(request, "home.html",{"menu_items": menu_items})
    return render(request, "restaurant_management/home.html", {
        "phone": settings.RESTAURANT_PHONE ,
        "restaurant_name": "Foodie's Paradise"
        
    })

def homepage(request):
    restaurant = Restaurant.objects.first()

    if restaurant:
        restaurant_name = restaurant.name
    else:
        restaurant_name = settings.restaurant_name
    
    context = {"restaurant_name": restaurant_nmae}
    return render(request, "home/index.html", context)

def custom_404(request, exception):
    context = {
        "request_path": request.path,
    }

    return render(request, "404.html", context=context, status=404)

def contact(request):
    return render(request, "contact.html")