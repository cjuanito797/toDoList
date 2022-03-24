from django.shortcuts import render, redirect, reverse
from .models import list, item
from .forms import ListForm, ItemForm, LoginForm, UserRegistration
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

# On the home page we can show a lists' webpage, for now we won't worry about user authentication
def home(request):
    my_lists = list.objects.filter (user_id=request.user)

    return render (request, '../templates/home/home.html', {'my_lists': my_lists})

def editProfile(reqeust):
    return render (reqeust, '../templates/userActions/editProfile.html')

def addNewTask(request):
    return render(request, '../templates/userActions/newTask.html')

def new_list(request):
    if request.method == "POST":
        list_form = ListForm (request.POST)

        if list_form.is_valid ( ):
            list = list_form.save ( )
            list.save ( )

            return redirect (reverse ('app:home'))

    else:
        list_form = ListForm ( )

    return render (request, "userActions/addList.html", {'list_form': list_form, })


def user_login(request):
    if request.method == 'POST':
        form = LoginForm (request.POST)

        if form.is_valid ( ):
            # clean the data

            cd = form.cleaned_data
            # perform an authenticatication on the user based off of the username and password grabbed from the form
            user = authenticate (request,
                                 username=cd['username'],
                                 password=cd['password'])

        # if the user does exist, meaning it is not None
        if user is not None:
            if user.is_active:
                login (request, user)
                return render (request, 'home/home.html')
            else:
                return HttpResponse ("Invalid Account")
        else:
            return HttpResponse ("Invalid Login")

    else:
        form = LoginForm ( )
        return render (request, 'registration/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistration (request.POST)
        if user_form.is_valid ( ):
            # Create a new user object but avoid saving it yet
            new_user = user_form.save (commit=False)
            # Set the chosen password
            new_user.set_password (
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save ( )
            Profile.objects.create (user=new_user)
            return render (request,
                           'registration/login.html',
                           {'new_user': new_user})
    else:
        user_form = UserRegistration ( )
    return render (request,
                   'registration/register.html',
                   {'user_form': user_form})
