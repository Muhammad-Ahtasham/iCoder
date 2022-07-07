from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('chal peya ea home')
def contact(request):
    return HttpResponse('chal peya ea contact')
def about(request):
    return HttpResponse('chal peya ea about')