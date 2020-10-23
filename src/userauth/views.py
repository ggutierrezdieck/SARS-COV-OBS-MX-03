from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CreateUser
# # Next lines only needed for default forms
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm

# Create your views here.

# Simple default user creation form

def registerUser(response):
    pass
    # if response.method == 'POST':
    #     registerForm = CreateUser(response.POST)
    #     if registerForm.is_valid():
    #         registerForm.save()
    #         return redirect(reverse('home'))
    # else:
    #     registerForm = CreateUser()
    #     return render(response, "session.html", {'form': registerForm})
