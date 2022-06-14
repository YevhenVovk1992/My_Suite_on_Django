from django.shortcuts import render, redirect
from .models import Artiles, motors
from .forms import ArtilesForm

# Create your views here.

def news_home(request):
    news = Artiles.objects.order_by('-date')
    base = {
        'title': 'News',
        'news': news
    }

    return render(request, 'news/news_home.html', base)

def catalog_motors(request):
    mtr = motors.objects.all()
    base = {
        'title': 'Catalog',
        'motors': mtr
    }
    return render(request, 'news/catalog_motors.html', base)

def add_new(request):
    error = ''
    if request.method == 'POST':
        data = ArtilesForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect("home")
        else:
            error = 'Incorrect'

    data = ArtilesForm()
    base = {
        'title': 'add new',
        'error': error,
        'form': data
    }
    return render(request, 'news/add_new.html', base)