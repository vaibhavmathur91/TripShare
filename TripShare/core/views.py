from django.shortcuts import render


# Create your views here.
def landing_page(request):
    if request.user.is_authenticated:
        context = {}
        return render(request, './blog/home_page.html', context)
    else:
        context = {}
        return render(request, 'core/landing_page.html', context)
