from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import SignUpForm, LoginForm


# Create your views here.
def index(request):
    data = {
        'title': ' MOTO VOVK '
    }
    return render(request, 'mainapp/index.html', data)


def about(request):
    data = {
        'title': "About",
        'countries': ('Ukraine', 'Hungary', 'Slovenia', 'Austria', 'Bulgaria', 'Romania')
    }
    return render(request, 'mainapp/about.html', data)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> We can not found this page!</h1>')


def user_registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SignUpForm()

    data = {
        'form': form,
        'title': 'registration'
    }
    return render(request, 'mainapp/user_registration.html', data)

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disable account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm

    data = {
        'form': form,
        'title': 'Login'
    }
    return render(request, 'mainapp/login.html', data)
