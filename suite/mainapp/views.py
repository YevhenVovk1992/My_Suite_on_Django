from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import SignUpForm


# Create your views here.
def index(request):
    data = {
        'title': ' MOTO VOVK ',
        'countries': ('Ukraine', 'Hungary', 'Slovenia', 'Austria', 'Bulgaria', 'Romania')
    }
    return render(request, 'mainapp/index.html', data)


def about(request):
    data = {
        'title': "About"
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