from django.shortcuts import render
from django.views import View
import pandas as pd
import numpy as np

from django.views.generic import ListView, DetailView
from .models import Article



df = pd.read_csv("datatable/data/data-csv.csv")
# Render the Home page
class Home(View):
    def get(self, request):
        return render(request, 'datatable/home.html')

    def post(self, request):
        return render(request, 'datatable/home.html')


# Render the Home page
class Table(View):
    
    def get(self, request):
        data = [[1,2,3,4],[1,2,3,4]]
        temp = df
        articles = Article.objects.all()
        return render(request, 'datatable/table.html',{'dataT':data, 'articles':articles, 'temp':temp})

    def post(self, request):
        articles = Article.objects.all()
        title = request.POST.get('title')
        body = request.POST.get('body')
        data = {
            'title': title,
            'body': body
        }
        Article.objects.create(**data)
        print(title, body,"Save.............")
        return render(request, 'datatable/table.html',{'dataT':data, 'articles':articles})


# Render the Home page
class ArticleListView(View):
    def get(self, request):
        articles = Article.objects.all()
        return render(request, 'datatable/article_list.html', {'articles': articles})

    def post(self, request):
        return render(request, 'datatable/article_list.html')

# class ArticleListView(ListView):
#     model = Article
#     template_name = "datatable/article_list.html"


class ArticleDetailView(View):
    def get(self, request, slug):
        article = Article.objects.get(slug=slug)
        return render(request, 'datatable/article_detail.html', {'article': article})

    def post(self, request, slug):
        return render(request, 'datatable/article_detail.html')

# class ArticleDetailView(DetailView):
#     model = Article
#     template_name = "datatable/article_detail.html"
     
     
class Ajaxpage(View):
    def get(self, request):
        return render(request, 'datatable/ajaxhtml.html')

    def post(self, request):
        return render(request, 'datatable/ajaxhtml.html')