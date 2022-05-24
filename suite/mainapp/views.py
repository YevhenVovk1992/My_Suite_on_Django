from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h4> проверка работы mainapp/view.py при обращении к главной страницы</h4>")

def about(request):
    return HttpResponse("<h5>Страница про нас</h5>")