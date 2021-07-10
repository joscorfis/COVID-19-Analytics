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
    path('lista-primeros-repositorios/', views.lista_primeros_repositorios),
    path('lista-mas-actualizados/', views.lista_mas_actualizados),
    path('grafica-de-evolucion/', views.grafica_de_evolucion),
    path('lista-mas-proyectos/', views.lista_mas_proyectos),
    path('show/<str:name_owner>', views.show),
]