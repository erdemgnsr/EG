from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib import messages
from .models import Blog, Blog_Category


"""def index(request):
    return render(request,"index.html")"""

def blogs(request):
    blogs = Blog.objects.filter(published=True)
    context = {
        "blogs" : blogs
    }
    return render(request,"blogs.html",context)

def category(request,category):
    blogs = Blog.objects.filter(published=True, category__url = category)
    context = {
        "blogs" : blogs
    }
    return render(request,"blogs.html",context)

def single(request,id):
    blogs = Blog.objects.filter(published=True, id = id)
    content_list = []
    quote_list = []
    for blog in blogs:
        content_list = (blog.content.split("\n" or "\r"))
        quote_list = (blog.quote.split("\n" or "\r"))
    context = {
        "blogs" : blogs,
        "content_list" : content_list,
        "quote_list" : quote_list
    }
    return render(request,"single.html",context)

"""def filtered_blogs(request):
    blogs = Blog.objects.filter(published=True and category=request.GET.get("name"))
    context = {
        "blogs" : blogs
    }
    return render(request,"blogs.html",context)"""
