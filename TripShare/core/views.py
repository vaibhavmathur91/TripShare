from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def landing_page(request):
    if request.user.is_authenticated:
        return redirect('blog')
    else:
        context = {}
        return render(request, 'core/landing_page.html', context)


def register_user(request):
    if request.method == 'POST':
        first = request.POST.get('FirstSignUp')
        last = request.POST.get('LastSignUp')
        email = request.POST.get('EmailSignUp')
        password = request.POST.get('PasswordSignUp')
        try:
            User.objects.get(username=email)
            messages.error(request, 'Email Already Exist!!', extra_tags='SignUpError')
            return redirect('/')
        except User.DoesNotExist:
            user = User.objects.create_user(email, email, password)
            user.first_name = first
            user.last_name = last
            user.save()
            return HttpResponseRedirect('blog')
    else:
        messages.error(request, 'Wrong Method Type!!', extra_tags='SignUpError')
        return redirect('/')


def login_user(request):
    import pdb;pdb.set_trace()
    email = request.POST.get('EmailSignIn')
    password = request.POST.get('PasswordSignIn')
    user = authenticate(username=email, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('blog')
    else:
        messages.error(request, 'Wrong Input!!', extra_tags='SignInError')
        return redirect('/')


def logout_user(requset):
    logout(requset)
    context = {}
    return render(requset, 'core/landing_page.html', context)
