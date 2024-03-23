from django.shortcuts import render
from articles.models import Articles

def home(request):
    articles = Articles.objects.all().filter(is_available=True)
    context = {
        'articles': articles,
    }
    return render(request, "home.html", context)