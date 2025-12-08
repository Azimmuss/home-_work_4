from django.urls import path
from . import views


urlpatterns = [
    path('aloo/', views.helloWordViews, name='aloo'),
    path('quotes/', views.quotesView, name='quotes'),
    path('time/', views.timeView, name ='time'),  


]