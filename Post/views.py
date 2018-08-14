from django.shortcuts import render
from django.http import HttpResponse
from Post.models import Post, Category

def simple_listPage(request):
    AllPost = Post.objects.all()
    AllCategory = Category.objects.all()
    resulSTR = ''
    for postOb in AllPost:
        resulSTR = resulSTR + postOb.header + ' '
        categoryList = AllCategory.filter(post = postOb)
        for categor in categoryList:
            resulSTR = resulSTR + categor.name + ' '
    return HttpResponse(resulSTR)

def listPage(request):
    return render(request, 'Post/test.html')