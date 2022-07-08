from turtle import title
from django.shortcuts import render, HttpResponse
from home.models import Contact
from blog.models import Post
from django.contrib import messages 
# Create your views here.
def home(request):
    return render(request, 'home/home.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        msg = request.POST['content']
        if len(name)<2 or len(email)<10 or len(phone)<11:
            messages.error(request, 'Please Enter Correct Form')
        else:
            messages.success(request, 'Your message has been sent')
            contact = Contact(name=name, email = email, phone = phone, content = msg)
            contact.save()
        print(name, email, phone, msg)
    return render(request, 'home/contact.html')
def about(request):
    return render(request, 'home/about.html')
def search(request):
    query = request.GET['query']
    allPosts = Post.objects.filter(title__icontains = query)
    params = {
        'allPosts': allPosts
    }
    return render(request, 'home/search.html', params)
 