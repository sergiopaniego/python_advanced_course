# mi_app/urls.py
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', views.BookViewSet)

urlpatterns = [
    path('', views.home, name='home'),  # Route to main page of the application
    path('about/', views.about, name='about'),  # Route to "about" page
    path('api_data/', views.api_data, name='api_data'),  # Route to "about" page
    path('authors/', views.author_view, name='author_view'),
    path('profile/', views.profile, name='profile'),
    path('about_2/', views.about_2, name='about_2'),
    path('base_with_logo/', views.base_with_logo, name='base_with_logo'),
    path('base_with_js/', views.base_with_js, name='base_with_js'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('protected_profile/', views.protected_profile, name='protected_profile'),
    path('', include(router.urls)),
    path('api_authors/', views.AuthorListCreateView.as_view(), name='author-list-create'),
    path('api_authors/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
]
