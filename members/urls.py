from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('book/', views.book, name='book'),
    path('llogin/', views.llogin, name='llogin'),
]