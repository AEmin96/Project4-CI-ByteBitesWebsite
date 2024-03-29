from django.urls import path
from . import views

urlpatterns = [
    
    path('book/', views.book, name='book'),
    path('mybookings', views.mybookings, name='mybookings'),
    path('booking/<int:booking_id>/update/', views.update_booking, name='update_booking'),
    path('booking/<int:booking_id>/delete/', views.delete_booking, name='delete_booking'),
    path('newbook/', views.newbook, name='newbook'),
    path('updatebkng/<int:book_id>', views.updatebkng, name='updatebkng'),
    path('addbk/', views.addbk, name='addbk'),
]