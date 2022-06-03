from django.shortcuts import render

# Create your views here.
def news_home(request):
    data = {
        'title': "News"
    }
    return render(request, 'news/news_home.html', data)

