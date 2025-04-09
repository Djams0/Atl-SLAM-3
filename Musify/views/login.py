from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User  

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        users = authenticate(request, username=email, password=password)
        if users is not None:

            login(request, users)
            return redirect('home') 
        else:
            messages.error(request, 'Email ou mot de passe incorrect.')

    return render(request, 'login.html')



