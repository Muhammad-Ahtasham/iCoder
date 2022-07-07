from django.http import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def blogHome(request):
    return HttpResponse('chal peya blog')
def blogPost(request, slug):
    return HttpResponse(f'chal peya blog {slug}')