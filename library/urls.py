from django.urls import path, re_path
from . import views


app_name = 'library'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.user_register, name='user_register'),
    path('books/', views.books, name='books'),
    path('book/<int:id>', views.book, name='book'),
    path('book/edit/<int:id>', views.edit, name='edit'),
    path('book/delete/<int:id>', views.delete, name='delete'),
    path('book/new/', views.new, name='new'),

]
