from django.urls import path
from . import views

urlpatterns = [
  path ('',views.create, name='create'),
  path ('delete/<int:id>',views.delete, name='delete'),
  path ('read/<int:id>',views.read, name='read'),
  path ('update/<int:id>/<str:headline>',views.update, name='update')
]