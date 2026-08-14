from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('produtos/', views.produtos, name='produtos'),
    path('categorias/', views.categorias, name='categorias'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
]