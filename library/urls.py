from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='library_index'),
    path('int/<int:br>', views.broj, name='library_broj'),
    path('int/', views.broj, name='library_broj_def'),
    path('rec/<str:rec>', views.rec, name='library_rec'),
    path('params/', views.params, name='library_params')
]
