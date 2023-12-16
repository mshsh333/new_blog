from django.shortcuts import render, redirect
from .models import Post, Category
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm


def index(request):
    posts = Post.objects.order_by('-date')[:10]
    categoies = Category.objects.all()
    return render(request, 'index.html', {'posts': posts, 'categories': categoies})

def post_detail(request, slug):
    post = Post.objects.get(slug__exact=slug)
    return render(request, 'post_detail.html', {'post':post})

def category_detail(request, slug):
    category = Category.objects.get(slug__exact=slug)
    return render(request, 'category_detail.html', {'category':category})

def search(request):
    query = request.GET.get('search')
    posts = Post.objects.filter(Q(title__iregex = query))
    content = {'posts': posts, "query":query}
    return render(request, 'search.html', content)

def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('index')
        else:
            form = RegisterForm()
        return render(request, 'register.html', {'form': form})
    return redirect('index')

def login_site(request):
    if request.user.is_authenticated:
        return redirect('index')
    message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            message = 'Извините такого пользователя нет'
        return render(request, 'login.html', {'message': message})
    return render(request, 'login.html', {'message': message})
    
def logout_site(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')