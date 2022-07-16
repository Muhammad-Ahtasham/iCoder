from django.shortcuts import redirect, render, HttpResponse
from blog.models import Post, BlogComment
from blog.templatetags import extras
from django.contrib import messages
# Create your views here.
def blogHome(request):
    allPosts = Post.objects.all()
    context = {
        'allPosts': allPosts
    }
    return render(request, 'blog/blogHome.html', context)
def blogPost(request, slug):
    post = Post.objects.filter(slug= slug).first()
    post.views = post.views + 1
    post.save()
    comments = BlogComment.objects.filter(post = post, parent = None)
    replies = BlogComment.objects.filter(post = post).exclude(parent = None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    context = {
        'post': post, 
        'comments': comments, 
        'user': request.user,
        'replyDict': replyDict
    }
    return render(request, 'blog/blogPost.html', context)

def postComment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.get(sno = postSno)
        parentSno = request.POST.get('parentSno')
        if parentSno == "":
            commentS = BlogComment(comment= comment, user = user, post = post)
            commentS.save()
            messages.success(request, 'Your Comment has been posted')
        else:
            parent = BlogComment.objects.get(sno = parentSno)
            commentS = BlogComment(comment= comment, user = user, post = post, parent = parent)
            commentS.save()
            messages.success(request, 'Your reply has been posted')
    return redirect(f'/blog/{post.slug}')