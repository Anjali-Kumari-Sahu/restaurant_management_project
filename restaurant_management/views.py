from django.shortcuts import render
 
def restaurant_about(request):
    
    return render(request, "restaurant_management/about.html")