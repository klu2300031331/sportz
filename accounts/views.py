from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# Updated registration view
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')  # Redirect to home page
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


# Define a custom LoginForm that adds Bootstrap classes
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

# Updated login view using the built-in AuthenticationForm
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home page
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid login credentials')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def user_details(request):
    return render(request, 'user_details.html', {'user': request.user})
