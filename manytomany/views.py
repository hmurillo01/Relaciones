from django.shortcuts import render
from django.http import HttpResponse
from.models import Publication, Article

def create (request):
  #creamos publicación
  # publi1 = Publication (title ="Mi primera publicación")
  # publi1.save()
  # publi2 = Publication (title ="Testing con cypress")
  # publi2.save()
  # publi3 = Publication (title ="Publicación Juan el haker")
  # publi3.save()
  # publi4 = Publication (title ="Mi otra publicación")
  # publi4.save()

  # art1= Article(headline = "Titular 1")
  # art1.save()
  # art2= Article(headline = "Titular 2")
  # art2.save()
  # art3= Article(headline = "Titular 3")
  # art3.save()
  publi1 = Publication.objects.get(id=1)
#   publi2 = Publication.objects.get(id=1)
#   publi3 = Publication.objects.get(id=1)
#   publi4 = Publication.objects.get(id=1)

  art1= Article.objects.get(id=1) 
#   art2= Article.objects.get(id=2)
#   art3= Article.objects.get(id=3)


# #relaciones
#   art1.publications.add(publi1)
#   art2.publications.add(publi2)
#   art3.publications.add(publi3,publi4)

  art1.publications.remove(publi1)

  return HttpResponse ("muchos a muchos")
#Consultamos
def consulta (resquest,id):
  post = Publication.objects.get (id=id)
  post2= Article.objects.get(id=id)
  #print(f'Publicación:{post.title}, headline:{post2.headline}')
  return HttpResponse (f"Titulo:{post.title} , headline:{post2.headline}")

#
def modificar(resquest,id, title):
  title = "llalalal"
  post = Publication.objects.get(id=id)
  post.title =title
  print(post.title)
  post.save()
  return HttpResponse (title)


def eliminar (request, id):
  post = Publication.objects.get(id=id)
  post.delete()
  return HttpResponse ("Post eliminado")
  

