from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'library/index.html', {'page_title': 'Library app'})
    else:
        return redirect('library_baza:books')


def books(request):
    tmp = Book.objects.all()
    return render(request, 'books.html', {'books': tmp})


def book(request, id):
    return None


def edit(request, id):
    return None


def new(request):
    return None