from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='library_index'),
    path('int/<int:br>', views.broj, name='library_broj'),
    path('int/', views.broj, name='library_broj_def'),
    path('rec/<str:rec>', views.rec, name='library_rec'),
    path('params/', views.params, name='library_params'),
    re_path(r'^regex/(?:godina-(?P<godina>[0-9]{4}))/(?:mesec-(?P<mesec>[0-9]{2}))', views.regex, name='library_regex'),
    path('hello/', views.hello, name='library_hello'),
]
