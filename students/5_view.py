   # Views -> send data to templates return back browser
   
from django.shortcuts import render

def home(request):
    context = {
        "name" : "Sam sophal",
        "Course" : "Django Programing",
        "start" : "08-04-2024",
        
    };
    
    
    return render(request, 'home.html', context);
    