from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
def index(request):
    data = {
        'title': ' MOTO VOVK ',
        'countries': ('Ukrane', 'Hungary', 'Slovenia', 'Austria', 'Bulgaria', 'Romania')
    }
    return render(request, 'mainapp/index.html', data)

def about(request):
    data = {
        'title': "About"
    }
    return render(request, 'mainapp/about.html', data)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> We can not found this page!</h1>')