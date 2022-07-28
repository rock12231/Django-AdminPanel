from django.urls import path
from datatable.views import Home, Table, ArticleListView, ArticleDetailView, Ajaxpage

urlpatterns = [
    
        # Index page URL
        path('', Home.as_view(), name='home'),
        path('table/', Table.as_view(), name='table'),
        path("avi/<slug:slug>", ArticleDetailView.as_view(), name="article_detail"),
        path("avi/", ArticleListView.as_view(), name="article_list"),
        path("ajax/", Ajaxpage.as_view(), name="ajaxhtml"),
        

]
