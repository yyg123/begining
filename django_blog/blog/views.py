from django.shortcuts import render,render_to_response
from django.shortcuts import render
from django.http import HttpResponse
# from blog.models import Article

from .models import BlogPost
from .models import *
from .forms import CommentForm
from django.http import Http404
# Create your views here.

def welcome(request):
    return render(request,'welcome.html')

def index(request):
    post_lists = Article.objects.all()
    return render(request, 'index.html', {'post_lists':post_lists})

def detail(request, num):
    try:
        post_list = BlogPost.objects.get(id = int(num))
        return render(request, 'detial.html', {'post_list': post_list})
    except Exception as e:
        print(e)
    return HttpResponse(num)

def myBlog(request):
    blog_list=BlogPost.objects.all()
    return render_to_response('BlogTemplate.html',{'blog_list':blog_list})




def get_blogs(request):                        #该模块用于view.py模块以及具体博客评论
    blogs=Blog.objects.all().order_by('-pub')#获得所有的博客按时间排序
    return render_to_response('blog_list.html',{'blogs':blogs})#传递context:blog参数到固定页面。

def get_details(request,blog_id):
#检查异常
    try:
        blog=Blog.objects.get(id=blog_id)#获取固定的blog_id的对象；
    except Blog.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        form = CommentForm()
    else:#请求方法为Post
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data=form.cleaned_data
            cleaned_data['blog']=blog
            Comment.objects.create(**cleaned_data)
    ctx={
        'blog':blog,
        'comments': blog.comment_set.all().order_by('-pub'),
        'form': form
    }#返回3个参数
    return render(request,'blog_details.html',ctx)