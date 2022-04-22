
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import NewUserForm,ProfileUpdateForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.decorators import login_required




@login_required
def update_profile(request):
    if request.method == 'POST':
        user = NewUserForm(request.POST)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",user)
        profile_form = ProfileUpdateForm(request.POST)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",profile_form)
        
        if user.is_valid() and profile_form.is_valid():
            user_d = user.save(commit=False)

            profile = profile_form.save(commit=False)

            profile.user_d = user_d

            user_d.save()
            profile.save()

            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('login')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user = NewUserForm()
        profile = ProfileUpdateForm()
    return render(request, 'register.html', {
        'user': user,
        'profile': profile_form
    })

    


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        print("🚀 ~ file: views.py ~ line 47 ~ form", form)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print("form.cleaned_data")
            
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(
                    request, f"You are now logged in as {username}.")
                return redirect('home')
        
            else:
                messages.error(request, "Invalid username or password.")
    else:
        messages.error(request, "Invalid username or password.")
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})


def home(request):
    return render(request, "home.html")