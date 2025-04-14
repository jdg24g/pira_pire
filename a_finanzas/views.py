from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse

# Create your views here.

def index(request):
    title = 'Pira Pire'
    context = {
        'title':title
    }
    return render(request,'index.html',context)