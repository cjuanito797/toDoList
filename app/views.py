from django.shortcuts import render, redirect
from .models import list, item


# Create your views here.

# On the home page we can show a lists' webpage, for now we won't worry about user authentication
def home(request):
    my_lists = list.objects.all()

    return render (request, '../templates/home/home.html', {'my_lists' : my_lists})
