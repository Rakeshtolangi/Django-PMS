from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):
    my_index = {'index_me' : 'This is from index function.'}
    return render(request, 'index.html', context = my_index)