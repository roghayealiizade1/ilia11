from django.shortcuts import render
import reverse
from django.http import HttpResponse
import requests

# Create your views here.

c_list=[
    {"id": 1,"name":"pyrhon"},
    {"id": 2,"name":"c++"},
    {"id": 3,"name":"c"},
    {"id": 4,"name":"c#"}
]


def course(request):
    id=request.GET.get('id','0')
    for item in c_list:
        if item['id'] in c_list:
            return render(request,'ilia/ilia.html')
        else :
            return render(request,'notfoundapp/4041.html')
              