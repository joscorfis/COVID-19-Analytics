from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('lista-mas-visualizados/', views.lista_mas_visualizados),
    path('lista-mas-forks/', views.lista_mas_forks),
    path('lista-mas-estrellas/', views.lista_mas_estrellas),
    path('lista-mejores-lenguajes/', views.lista_mejores_lenguajes),
    path('show/1', views.show),
]