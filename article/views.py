from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from .models import Article
from django import forms

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','content','category']

def home(request):
    s = ''
    for article in Article.objects.all():
      s += """<h1>{0}</h1>
            {1}
            """.format(article.title,article.content)
    return HttpResponse(s)

def detail(request,pk):
    article = Article.objects.get(pk= int(pk))
    return render(request,"detail.html",locals())

def create(request):
  if request.method == 'POST':
    form = ArticleForm(request.POST)
    if form.is_valid():
        new_article = form.save()
        return redirect('/article/'+str(new_article.pk))
        # return HttpResponseRedirect('/article/'+str(new_article.pk))
 
  form = ArticleForm()
  return render(request,'create.html',locals())