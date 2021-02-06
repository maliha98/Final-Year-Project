from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from .forms import *


def seller_signInPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'seller_signin.html')


def seller_logoutPage(request):
    logout(request)
    return redirect('seller_signin')


def seller_signUpPage(request):

    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('seller_signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('seller_signup')
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()

                return redirect('seller_signin')

        else:
            messages.info(request, 'password not matching..')
            return redirect('seller_signup')
        return redirect('/')

    else:
        return render(request, 'seller_signup.html')


@login_required
def seller_profilePage(request):
    seller = request.user.seller
    form = SellerForm(instance=seller)

    if request.method == 'POST':
        form = SellerForm(request.POST, request.FILES, instance=seller)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'seller_profile.html', context)
