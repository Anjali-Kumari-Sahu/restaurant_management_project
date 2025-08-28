from django.shortcuts import render
from django.db import DatabaseError
from .models import Restaurant 
 
def restaurant_about(request):
    try:
        restaurant = Restaurant.objects.first()


        if restaurant:
            restaurant_name = restaurant.restaurant_name
            restaurant_address = restaurant.restaurant_address
            restaurant_phone = restaurant.restaurant_phone
        else:
            restaurant_name = "Foodie's Paradise"
            restaurant_address = "Address not available"
            restaurant_phone = "Phone not available"

    except DatabaseError:

        restaurant_name = "Foodie's Paradise"
        restaurant_address = "Error: could not fetch address"
        restaurant_phone = "Error: Could not fetch phone"
    


    return render(request, "restaurant_management/about.html", {
        "restaurant_name": restaurant_name,
        "restaurant_address": restaurant_address,
        "restaurant_phone": restaurant_phone,
    })