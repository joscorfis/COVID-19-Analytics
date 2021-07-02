from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('lista-mas-visualizados/', views.lista_mas_visualizados),
    path('show/1', views.show),
]