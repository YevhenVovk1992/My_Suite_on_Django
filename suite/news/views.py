from django.shortcuts import render, redirect
from .models import Artiles, motors
from .forms import ArtilesForm
from django.views.generic import DetailView, UpdateView, DeleteView

# Create your views here.

def news_home(request):
    news = Artiles.objects.order_by('-date')
    base = {
        'title': 'News',
        'news': news
    }

    return render(request, 'news/news_home.html', base)

class NewsDetailView(DetailView):
    model = Artiles
    template_name = 'news/detail_view.html'
    context_object_name = 'artiles'

class NewsUpdateView(UpdateView):
    model = Artiles
    template_name = 'news/add_new.html'
    form_class = ArtilesForm

class NewsDeleteView(DeleteView):
    model = Artiles
    success_url = '/news/'
    template_name = 'news/new_delete.html'

def catalog_motors(request):
    mtr = motors.objects.all()
    base = {
        'title': 'Catalog',
        'motors': mtr
    }
    return render(request, 'news/catalog_motors.html', base)

class InfCatalogMotors(DetailView):
    model = motors
    template_name = 'news/inf_catalog.html'
    context_object_name = 'motors'

def add_new(request):
    error = ''
    if request.method == 'POST':
        data = ArtilesForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect("news_home")
        else:
            error = 'Incorrect'

    data = ArtilesForm()
    base = {
        'title': 'add new',
        'error': error,
        'form': data
    }
    return render(request, 'news/add_new.html', base)