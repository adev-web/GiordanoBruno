from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages


def signup(request):
    if request.method == 'GET':
        return render(request, 'secure/signup.html', {
            'form': UserCreationForm,
            'tittle': 'Sign-Up'})
    else:
        if (request.POST['password1'] == request.POST['password2']):
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('main')
            except:
                return render(request, 'secure/signup.html', {
                    'form': UserCreationForm,
                    'tittle': 'SignUp',
                    'error': 'Username already exists'})
        else:
            return render(request, 'secure/signup.html', {
                'form': UserCreationForm,
                'tittle': 'SignUp',
                'error': "password don't match"})


def signin(request):
    if request.method == 'GET':
        return render(request, 'secure/signin.html', {
            'form': AuthenticationForm,
            'tittle': 'SignIn'})
    else:
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password'])
        if (user is None):
            return render(request, 'secure/signin.html', {
                'form': AuthenticationForm,
                'tittle': 'SignIn',
                'error': 'Username or password is incorrect'})
        else:
            login(request, user)
            return redirect('main')
        
@login_required
def signout(request):
    logout(request)
    return redirect('main')
