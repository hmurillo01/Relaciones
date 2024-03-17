from django.urls import path
from . import views

urlpatterns = [
  path ('',views.create, name='create'),
  path ('consulta/<int:id>',views.consulta, name='consulta'),
  path ('modificar/<int:id>/<str:title>',views.modificar, name='modificar'),
  path ('eliminar/<int:id>',views.eliminar,name='eliminar'),

]