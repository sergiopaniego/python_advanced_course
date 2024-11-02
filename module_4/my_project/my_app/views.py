# views.py
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import Author, Book
from .forms import AuthorForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, generics
from .serializers import BookSerializer, AuthorSerializer


def home(request):
    return HttpResponse("Welcome to the Home Page")

def about(request):
    return render(request, 'my_app/about.html')


def api_data(request): 
    data = { "name": "Sergio", "age": 30, "city": "Madrid" } 
    return JsonResponse(data) 


def author_view(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_view') 
    else:
        form = AuthorForm()

    authors = Author.objects.all()  # Obtiene todos los autores
    return render(request, 'my_app/authors.html', {'form': form, 'authors': authors})

from django.shortcuts import render

def profile(request):
    context = {
        'username': 'Sergio',
        'is_active': True,
        'projects': [
            {'name': 'Project A', 'status': 'Completed'},
            {'name': 'Project B', 'status': 'In Progress'},
            {'name': 'Project C', 'status': 'Not Started'}
        ]
    }
    return render(request, 'my_app/profile.html', context)


def about_2(request):
    return render(request, 'my_app/about_2.html')

def base_with_logo(request):
    return render(request, 'my_app/base_with_logo.html')

def base_with_js(request):
    return render(request, 'my_app/base_with_js.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')  # Redirects the user to the login page
    else:
        form = UserCreationForm()
    return render(request, 'my_app/register.html', {'form': form})


@login_required
def protected_profile(request):
    return render(request, 'my_app/protected_profile.html')



class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer