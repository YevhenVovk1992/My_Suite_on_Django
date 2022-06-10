from django.shortcuts import render
from .models import Artiles, motors

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
