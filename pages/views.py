from typing import final
from django.shortcuts import render
from django.views.generic import TemplateView
from articles.models import Article


def HomePageView(request):
     if request.user.is_authenticated:
          current_user= request.user
          return render(request,'users/home.html',{'iter':Article.objects.filter(author=current_user)})
     else:
          return render(request,'users/home.html')


