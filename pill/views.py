import json

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .models import User
from .signals import create_profile
from django.http import HttpResponse

def register(request):
    if request.method == 'GET':
        # form = UserRegisterForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     username = form.cleaned_data.get('username')
        #     messages.success(request, f'Your account has been created! You are now able to log in')
        #     return redirect('login')
        form = UserRegisterForm()
    # else:
    #     form = UserRegisterForm()
    return render(request, 'auth/register.html', {'form': form})


def save_user(request):
    if request.method == 'POST':
        try:

            form = UserRegisterForm(request.POST)
            # import pdb
            # pdb.set_trace()
            if form.is_valid():
                form.save()
                print("hiii")
                create_profile(request.POST.get('email'), request.POST.get('role'))
                print("AA")
                messages.success(request, f'Your account has been created! You are now able to log in')
                return redirect('home')
        except Exception as e:
                messages.success(request, f'Your account Failed')
    else:
        form = UserRegisterForm()
    return render(request, 'auth/register.html', {'form': {}})

@login_required()
def home(request):
    print (request.user.has_perm('ppview'))
    return HttpResponse(json.dumps({"msg":request.user.has_perm('ppview')}))

from . import forms
from django.contrib.auth import login, authenticate  # add to imports
def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                email=request.POST['username'],
                password=request.POST['password'],
            )
            print("user", user)
            if user is not None:
                login(request, user)
                message = f'Hello {user.username}! You have been logged in'
                print("jiiiii")
                return redirect('home')
            else:
                message = 'Login failed!'
                print("ellll")
                return redirect('login_page')
            # return redirect('home')
    else:
        return render(
            request, 'auth/login.html', context={'form': form, 'message': message})