from django.urls import path, re_path
from . import views


app_name = 'library_baza'
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.books, name='books'),
    path('book/<int:id>', views.book, name='book'),
    path('book/edit/<int:id>', views.edit, name='edit'),
    path('book/new/', views.new, name='new'),
]
