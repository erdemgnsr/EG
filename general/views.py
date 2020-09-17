from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib import messages
from blog.models import Blog

def index(request):
    blogs = Blog.objects.filter(published=True)
    context = {
        "blogs" : blogs[:3]
    }
    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request, "contact.html")