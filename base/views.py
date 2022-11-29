from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .models import Article, Comment
from .form import ArticleForm, CreateUserForm, CommentForm
from django.contrib.auth.forms import UserCreationForm  
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def RegisterUser(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    context = {'form':form}
    return render(request, 'base/signup.html', context)

def LoginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')

    context = {}
    return render(request, 'base/login.html' , context)

@login_required(login_url='/login')
def LogoutUSer(request):
    logout(request)
    return redirect('home')

def Home(request):
    blogs = Article.objects.filter(status=1).order_by('-created_at')[0:3]
    context = {'blogs':blogs}
    return render(request,'base/home.html',context)
def BlogList(request):
    blogs = Article.objects.filter(status=1).order_by('-created_at')[0:15]
    context = {'blogs':blogs}
    return render(request,'base/blogs.html',context)

def article(request, slug):
    blogs = Article.objects.filter(status=1).order_by('-created_at')[3:6]
    blog = Article.objects.get(slug=slug)
    comments = blog.comment_set.all()[:3]
    commentform = CommentForm()
    if request.method == "POST":
        commentform = CommentForm(request.POST)
        article = get_object_or_404(Article, slug=slug)
        if commentform.is_valid():
            commentl = commentform.save(commit=False)
            commentl.owner = request.user
            commentl.article = article
            commentform.save()

    context = {'blog':blog,'comments':comments,'commentform':commentform,'blogs':blogs}
    return render(request, 'base/article.html', context)
@login_required(login_url='/login')
def CreateArticle(request):
    form = ArticleForm()
    if request.method == "POST":
        
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            form.save()
            return redirect('home')
            
    context = {'form':form}
    return render(request, 'base/create_update.html', context)

@login_required(login_url='/login')
def UpdateArticle(request, slug):
    article = Article.objects.get(slug=slug)
    form = ArticleForm(instance=article)
    if request.user != article.author:
        return HttpResponse("you can't update this room")
    
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'base/create_update.html', context)
@login_required(login_url='/login')
def DeleteArticle(request, pk):
    article = Article.objects.get(id=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('home')

    return render(request, 'base/delete.html', {'obj':article})
