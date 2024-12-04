from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django import forms


def logout_view(request):
    logout(request)
    return redirect("home")
