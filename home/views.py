from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from blog.models import Post
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
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
    return render(request, 'home/contact.html')
def about(request):
    return render(request, 'home/about.html')
def search(request):
    query = request.GET['query']
    if len(query)>70:
        allPosts = Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsContent.union(allPostsTitle)
    if allPosts.count() == 0:
        messages.warning(request, 'No results Found')
    params = {
        'allPosts': allPosts,
        'query': query
    }
    return render(request, 'home/search.html', params)
 
def handleSignUp(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        #CHECKS FOR ERRORONUS INPUTS
        if len(username)>10:
            messages.error(request, "user name must be less than 10 characters")
            return redirect('/')
        if not username.isalnum():
            return messages.error(request, "user name should only contains letters and numerics")
            redirect('/')
        if pass1 != pass2:
            return messages.error(request, "Passwords donot match")
            redirect('/')
        #CREATE USER
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, "Your iCoder account has successfully been created")
        return redirect('/')
    else:
        return HttpResponse('404-Error Not Found')

def handleLogIn(request):
    if request.method == 'POST':
        loginUserName = request.POST['loginusername']
        loginPass = request.POST['loginpass']
        user = authenticate(username = loginUserName, password = loginPass)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('/')
        else:
            messages.error(request, "Ivalid Credentials, Try Again")
            return redirect('/')
def handleLogOut(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('/')