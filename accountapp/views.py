from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(request):
    if request.method == "POST":
        return render(request, 'accountapp/hello_world.html', context={'text': 'POST METHOD!!!'})
    else:
        return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD!!!'})

#render는 Templates에서 response를 가져옴

#기본적인 출력을 해주는 view