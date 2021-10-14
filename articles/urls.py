from django.urls import path
from .views import (
ArticleListView,
ArticleUpdateView,
ArticleDetailView,
ArticleDeleteView,
ArticleCreateView,
ArticleSearchView, 
Comm,
)

urlpatterns = [
path('<int:pk>/edit/',
ArticleUpdateView.as_view(), name='article_edit'), # new
path('<int:pk>/',
ArticleDetailView.as_view(), name='article_detail'), # new
path('<int:pk>/delete/',
ArticleDeleteView.as_view(), name='article_delete'), # new
path('', ArticleListView.as_view(), name='article_list'),
path('new/', ArticleCreateView.as_view(), name='article_new'),
path(r'search/', ArticleSearchView, name='article_search'),
path('<int:pk>/comment/',Comm.as_view(),name='com'),
]



