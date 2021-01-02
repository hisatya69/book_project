from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Zdravo !')


def broj(request, br):
    return HttpResponse('Broj: '+ str(br))
