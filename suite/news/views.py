from django.shortcuts import render, redirect
from .models import Artiles, motors
from .forms import ArtilesForm

# Create your views here.

def news_home(request):
    base = {
        'title': 'News'
    }
    news = Artiles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news, 'base': base})

def catalog_motors(request):
    base = {
        'title': 'Catalog'
    }
    mtr = motors.objects.all()
    return render(request, 'news/catalog_motors.html', {'motors': mtr, 'base': base})

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
        'error': error
    }
    return render(request, 'news/add_new.html', {'base': base, 'form': data})