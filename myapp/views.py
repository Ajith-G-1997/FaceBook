from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm, ProfileForm, PostForm,SignInForm
from .models import User, Profile, Post
from django.contrib import messages
from django.contrib.auth import authenticate, login


def home(request):
    return render(request,'base.html')

def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
           
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            
            return redirect('user_dashboard')  
    else:
        form = SignInForm()
    
    return render(request, 'signin.html', {'form': form})

def user_dashboard(request):
    return render(request,'user_dashboard.html')

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

def user_detail(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'user_detail.html', {'user': user})


def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        form = UserForm()
    
    return render(request, 'user_form.html', {'form': form})


def user_update(request, username):
    user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'user_form.html', {'form': form})

def user_delete(request, username):
    user = get_object_or_404(User, username=username)
    user.delete()
    return redirect('user_list')

def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'profile_list.html', {'profiles': profiles})

def profile_detail(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    return render(request, 'profile_detail.html', {'profile': profile})

def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = ProfileForm()
    return render(request, 'profile_form.html', {'form': form})

def profile_update(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profile_form.html', {'form': form})

def profile_delete(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    profile.delete()
    return redirect('profile_list')

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {'post': post})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # Replace 'post_list' with the URL name for the post list view
    else:
        form = PostForm()
    
    return render(request, 'post_form.html', {'form': form})

def post_update(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'post_form.html', {'form': form})

def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('post_list')
