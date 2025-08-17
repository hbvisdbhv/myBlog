from django.shortcuts import render
from app.models import*


def post_list (request):
    posts = Post.objects.all()
    
    return render(request, 'app/post_list.html', {'posts': posts})
