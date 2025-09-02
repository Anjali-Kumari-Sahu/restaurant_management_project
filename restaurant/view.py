from django.shortcuts import render

def menu_list(request):
    menu_items = [
        {"id":1, "name": "Margherita pizza","price": 250},
        {"id":2, "name": "Paneer Butter Masala" ,"price": 300},
        {"id":3, "name": "Veg Biriyani " ,"price":200},
        {"id":4, "name": " Masala Dosa","price" : 150},
        {"id":5, "name":  "  Cold Coffe ","price":120},
    ]

    return render(request, "menu.html", {"items": menu_items})

def reservations(request):
    try:
        return render(request, "restaurant/reservations.html")
    except Exception as e:
        return render(request, "restaurant/error.html",  {"error": str(e)})