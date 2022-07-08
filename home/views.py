import email
from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    return render(request, 'home/home.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        msg = request.POST['content']
        contact = Contact(name=name, email = email, phone = phone, content = msg)
        contact.save()
        print(name, email, phone, msg)
    return render(request, 'home/contact.html')
def about(request):
    return render(request, 'home/about.html')