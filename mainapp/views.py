from django.shortcuts import render
from datetime import datetime

# Create your views here.

def home(request):
    context = {}
    date = datetime.now().date()
    context["date"] = date
    return render(request ,"pages/home.html", context)

def about(request):
    return render(request ,"pages/about.html")

def contact(request):
    return render(request ,"pages/contact.html")
