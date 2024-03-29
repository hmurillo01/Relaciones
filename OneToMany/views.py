from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter, Article
from datetime import date

# Create your views here.
def create(request):
##  repo = Reporter(first_name="Juan", last_name="Arce", email="juanarcev1412@gmail.com")
## repo.save()

##  art1 = Article.objects.create(headline="Django basico", pub_date=date(2024,4,3), reporter=repo)
##  art2 = Article.objects.create(headline="Django intermedio", pub_date=date(2024,5,3), reporter=repo)
##  art3 = Article.objects.create(headline="Django avanzado", pub_date=date(2024,5,3), reporter=repo)

##return HttpResponse("Uno a muchos")

  repo = Reporter.objects.get(id=1)
  query = repo.article_set.all()

  return render (request, "index.html",{
  'repo':repo,
  'query':query
})

def read (request, id):
  
  reporter = Reporter.objects.get(id=id)
  
  query = reporter.article_set.all()
  
  return render(request, 'onetoone_read.html', {
    'reporter' : reporter,
    'query' : query
  })
  
  
def update(request, id, headline):
  article = Article.objects.get(id=id)
  article.headline = headline
  article.save()
  
  return HttpResponse('Datos actualizados correctamente.')


def delete(request, id):
  article = Article.objects.get(id=id)
  article.delete()
  
  return HttpResponse('Registro eliminado correctamente.')