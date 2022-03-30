from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, reverse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_control

from .forms import ListForm, UserRegistration, LoginForm, ItemForm
from .models import list, Profile, item

from django.shortcuts import render, redirect

from .forms import ItemModelFormset

def create_item_model_form(request, pk):
    list_instance = get_object_or_404 (list, pk=pk)
    template_name = 'userActions/newTask.html'
    heading_message = 'Add new toDo tasks below.'
    if request.method == 'GET':
        # we don't want to display the already saved model instances
        formset = ItemModelFormset(queryset=item.objects.none())
    elif request.method == 'POST':
        formset = ItemModelFormset(request.POST)
        if formset.is_valid():
            for item_form in formset:
                # only save if name is present
                if item_form.cleaned_data.get('task'):
                    item_instance = item_form.save(commit=False)
                    item_instance.save()
                    list_instance.item.add(item_instance)
            return redirect('app:home')
    return render(request, template_name, {
        'formset': formset,
        'heading': heading_message,
        'list_instance': list_instance
    })

# On the home page we can show a lists' webpage, for now we won't worry about user authentication
@login_required ( )
def home(request):
    my_lists = list.objects.filter (user_id=request.user)

    return render (request, '../templates/home/home.html', {'my_lists': my_lists})


@login_required ( )
def editProfile(reqeust):
    return render (reqeust, '../templates/userActions/editProfile.html')


@login_required ( )
def addNewTask(request):
    return render (request, '../templates/userActions/newTask.html')


@login_required ( )
def new_list(request):
    if request.method == "POST":
        list_form = ListForm (request.POST)

        if list_form.is_valid ( ):
            list = list_form.save (commit=False)
            # wait to save the newly created list until after we have, tied the list.user_id
            # to the id of the current logged-in user.
            list.user_id = request.user.id
            list.save ( )

            return redirect (reverse ('app:home'))

    else:
        list_form = ListForm ( )

    return render (request, "userActions/addList.html", {'list_form': list_form,})


@login_required ( )
def editList(request, pk):
    list_instance = get_object_or_404 (list, pk=pk)
    item_instances = list_instance.item.all ( )
    return render (request, 'userActions/editList.html')


@login_required ( )
def deleteList(request, pk):
    list_instance = get_object_or_404 (list, pk=pk)
    item_instances = list_instance.item.all ( )
    item_instances.delete ( )
    list_instance.delete ( )
    return redirect ('app:home')


@cache_control (no_cache=True, must_revalidate=True, no_store=True)
def login_request(request):
    if request.method == "POST":
        form = LoginForm (request.POST)
        if form.is_valid ( ):
            username = form.cleaned_data.get ('username')
            password = form.cleaned_data.get ('password')
            user = authenticate (username=username, password=password)
            if user is not None:
                login (request, user)
                return redirect ("app:home")
            else:
                messages.error (request, "Invalid username or password.")
        else:
            messages.error (request, "Invalid username or password.")
    form = LoginForm ( )
    return render (request=request, template_name="registration/login.html", context={"login_form": form})


@cache_control (no_cache=True, must_revalidate=True, no_store=True)
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
            login (request, new_user)
            return redirect ('app:home')
    else:
        user_form = UserRegistration ( )
    return render (request,
                   'registration/register.html',
                   {'user_form': user_form})


def logout_request(request):
    logout (request)
    messages.info (request, "You have successfully logged out.")
    return redirect ("app:login")
