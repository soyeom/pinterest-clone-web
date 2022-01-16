from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(request):
    return HttpResponse('Hello world!')

#기본적인 출력을 해주는 view