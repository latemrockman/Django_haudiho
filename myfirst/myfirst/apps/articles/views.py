from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Comment

# Create your views here.

def index(request):
    latest_articles_list = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'articles/list.html', {'all_articles': latest_articles_list})


def article_page(request, article_id):
    #return HttpResponse(f'Test - {article_id}')

    return render(request, 'articles/article_page.html', {})


def test(request):
    return HttpResponse('Test')



