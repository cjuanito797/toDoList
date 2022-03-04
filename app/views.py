from django.shortcuts import render, redirect


# Create your views here.

# On the home page we can show a lists' webpage, for now we won't worry about user authentication
def home(request):
    return render (request, '../templates/home/home.html')
