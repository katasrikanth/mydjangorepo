from django.http import request
from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView, DeleteView,CreateView
from .models import Article, Comment
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Article
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = Article
    template_name = 'articles/article_new.html'
    fields = ('title', 'body', )
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleListView(LoginRequiredMixin,ListView):
     model = Article
     template_name = 'articles/article_list.html'
     login_url = 'login'


def ArticleSearchView(request):
     current_user= request.GET['search']
     current_user=current_user.lower()
     f=Article.objects.all()
     for i in f:
          i.title=i.title.lower()
          i.save()
     final=Article.objects.filter(title=current_user)
     return render(request,'articles/article_search.html',{'iter':final})

class ArticleDetailView(DetailView):
     model = Article
     template_name = 'articles/article_detail.html'
     login_url = 'login'

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView): 
     model = Article
     fields = ('title', 'body',)
     template_name = 'articles/article_edit.html'
     login_url = 'login'

     def test_func(self):
          obj = self.get_object()
          return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView): 
    model = Article
    template_name = 'articles/article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'

    def test_func(self):
          obj = self.get_object()
          return obj.author == self.request.user

class Comm(LoginRequiredMixin ,CreateView):
     model = Comment
     template_name = 'articles/comment.html'
     fields = ('comment',)
     login_url = 'login'    
     
     def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.article =  Article.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)