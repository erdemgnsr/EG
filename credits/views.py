from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib import messages


"""def index(request):
    return render(request,"index.html")"""

def credits(request):
    return render(request,"credits.html")

def category(request,category):
    credits = Credits.objects.filter(published=True, category__url = category)
    context = {
        "credits" : credits
    }
    return render(request,"blogs.html",context)

def single(request,id):
    credits = Credits.objects.filter(published=True, id = id)
    content_list = []
    quote_list = []
    for credit in credits:
        content_list = (credit.content.split("\n" or "\r"))
        quote_list = (credit.quote.split("\n" or "\r"))
    context = {
        "cretits" : credits,
        "content_list" : content_list,
        "quote_list" : quote_list
    }
    return render(request,"single.html",context)