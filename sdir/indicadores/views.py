from django.shortcuts import render
from django.http import HttpResponse

def demo_vista_basica(request):
    return HttpResponse('Hola mundo2!!')
