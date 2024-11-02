# mi_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Route to main page of the application
    path('about/', views.about, name='about'),  # Route to "about" page
    path('api_data/', views.api_data, name='api_data'),  # Route to "about" page
    path('authors/', views.author_view, name='author_view'),
    path('profile/', views.profile, name='profile'),
    path('about_2/', views.about_2, name='about_2'),
    path('base_with_logo/', views.base_with_logo, name='base_with_logo'),
    path('base_with_js/', views.base_with_js, name='base_with_js'),
]
