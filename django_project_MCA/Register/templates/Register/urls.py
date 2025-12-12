from django.shortcuts import render, redirect
from .forms import RegisterForm


def register(request):
    form = RegisterForm()  # Instantiate the form
    return render(request, 'Register/register.html', {'form': form})

