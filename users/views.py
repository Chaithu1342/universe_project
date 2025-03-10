from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})

def dashboard(request):
    return render(request, 'users/dashboard.html')

## Step 5: Define URLs in `users/urls.py`

from django.urls import path
from .views import signup, dashboard

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('dashboard/', dashboard, name='dashboard'),
]
from django.shortcuts import render

def home(request):
    return render(request, 'users/home.html')
