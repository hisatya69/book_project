from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Zdravo !')


def broj(request, br=0):
    return HttpResponse('Broj: '+ str(br))


def rec(request, rec):
    return HttpResponse('Rec je: '+ rec)


def params(request):
    return HttpResponse('Params: '+str([str(k)+': '+str(v) for k, v in request.GET.items()]))


def regex(request, mesec, godina):
    return HttpResponse('Godina: '+ godina + ', Mesec: '+ mesec)


def hello(request):
    return render(request, 'library/hello.html')