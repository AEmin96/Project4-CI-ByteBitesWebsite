from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('llogin/', views.llogin, name='llogin'),
    path('', views.logout, name='logout')
]