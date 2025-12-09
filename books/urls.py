from django.urls import path
from . import views


urlpatterns = [
    path('aloo/', views.helloWordViews, name='aloo'),
    path('quotes/', views.quotesView, name='quotes'),
    path('time/', views.timeView, name ='time'),  
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),



]