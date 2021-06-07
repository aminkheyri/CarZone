from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'you logged in successfully')
            return redirect('accounts:dashboard')
        else:
            messages.error(request, 'Your Username or Password is incorrect')
            return redirect('accounts:login')
    return render(request, 'accounts/login.html')


def register(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username):
                messages.error(request, 'Username is already exists')
                return redirect('accounts:register')
            else:
                if User.objects.filter(email=email):
                    messages.error(request, 'Email is already exists')
                    return redirect('accounts:register')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email,
                                             username=username, password=password)
                    # auth.login(request, user)
                    # messages.success(request, 'you have logged in successfully')
                    # return redirect('accounts:dashboard')
                    user.save()
                    messages.success(request, 'You registered successfully now please login')
                    return redirect('accounts:login')

        else:
            messages.error(request, 'Your password must match')
            return redirect('accounts:register')

    return render(request, 'accounts/register.html')


def logout_user(request):
        logout(request)
        return redirect('pages:home')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')