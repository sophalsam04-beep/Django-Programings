from django.shortcuts import render

def home(request):
    return render(request, 'home.html');
    
    
def loadData(request):
    return render(request ,'template.html');

