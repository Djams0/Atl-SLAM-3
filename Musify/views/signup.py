
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login
from django import forms
from django.urls import reverse_lazy

# Formulaire d'inscription
class SignUpForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput,
    )

# Vue d'inscription
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Vérifiez si l'email existe déjà
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Cet email est déjà utilisé.')
                return render(request, 'signup.html', {'form': form})

            # Créez un nouvel utilisateur
            new_user = User.objects.create_user(
                username=email,  # Utilisation de l'email comme nom d'utilisateur
                email=email,
                password=password
            )
            new_user.first_name = first_name
            new_user.last_name = last_name
            new_user.save()

            # Connecte l'utilisateur
            login(request, new_user)

            messages.success(request, 'Inscription réussie. Vous êtes maintenant connecté.')
            return redirect('home')  # Redirige vers la page d'accueil après inscription

        else:
            messages.error(request, 'Veuillez vérifier les informations soumises.')
            return render(request, 'signup.html', {'form': form})

    else:
        form = SignUpForm()  # Affiche le formulaire vide pour GET
        return render(request, 'signup.html', {'form': form})  # Retourne le formulaire vide


