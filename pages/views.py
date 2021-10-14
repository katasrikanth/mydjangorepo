from typing import final
from django.shortcuts import render
from django.views.generic import TemplateView
from typing import final
from articles.models import Article

#class HomePageView(TemplateView):
   #  template_name = 'users/home.html'

def HomePageView(request):
     if request.user.is_authenticated:
          current_user= request.user
          final=Article.objects.filter(author=current_user)
          return render(request,'users/home.html',{'iter':final})
     else:
          return render(request,'users/home.html')


