from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib import messages


def landing_page(request):
    if request.user.is_authenticated:
        context = {}
        return render(request, './blog/home_page.html', context)
    else:
        context = {}
        return render(request, 'core/landing_page.html', context)


def register_user(request):
    if request.method == 'POST':
        import pdb;pdb.set_trace()
        first = request.POST.get('FirstSignUp')
        last = request.POST.get('LastSignUp')
        email = request.POST.get('EmailSignUp')
        password = request.POST.get('PasswordSignUp')
        try:
            user = User.objects.get(username=email)
            context = {'FirstSignUp': first, 'LastSignUp': last, 'EmailSignUp': email}
            messages.success(request, 'Profile details updated.')
            messages.error(request, 'Email Already Exist!!', extra_tags='SignUpError')
            return redirect('/', context)
        except User.DoesNotExist:
            user = User.objects.create_user(email, email, password)
            user.first_name = first
            user.last_name = last
            user.save()
            return redirect('blog')
    else:
        context = {}
        return render(request, 'core/landing_page.html', context)
