from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='library_index'),
    path('int/<int:br>', views.broj, name='library_broj')
]