from django.urls import path
from . import views

urlpatterns = [
  path ('',views.create, name='create'),
  path ('consultar/<int:id>',views.consultar, name='consultar'),
  path('modificar/<int:id>/<str:name>/<str:addres>/',views.modificar,name="modificar"),
  path('eliminar/<int:id>',views.eliminar,name="eliminar")

]