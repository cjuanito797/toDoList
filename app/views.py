from django.shortcuts import render, redirect, reverse
from .models import list, item
from .forms import ListForm, ItemForm


# Create your views here.

# On the home page we can show a lists' webpage, for now we won't worry about user authentication
def home(request):
    my_lists = list.objects.all()

    return render (request, '../templates/home/home.html', {'my_lists' : my_lists})

def new_list(request):
    if request.method == "POST":
        list_form = ListForm(request.POST)

        if list_form.is_valid():
            list = list_form.save()
            list.save()

            return redirect(reverse('app:home'))

    else:
        list_form = ListForm()

    return render(request, "../templates/userActions/addList.html", {'list_form' : list_form, })
