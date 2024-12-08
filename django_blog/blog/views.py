from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from blog.forms import UserRegistrationForm, UserUpdateForm, BlogPostsForm
from blog.models import Post



def index_view(request):
    context = {}
    return render(request, 'blog/base.html', context)


def register_view(request):
    register_form = UserRegistrationForm()

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        register_form = UserRegistrationForm(request.POST)

        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Registration succesful. You can now register.')
            return redirect('login')

    context = {'register_form': register_form}
    return render(request, 'blog/register.html', context)


def signin_view(request):
    login_form = AuthenticationForm()

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = authenticate(request, username=username, password=password)

            if user is None:
                messages.error(request, 'Invalid credentials')

            else:
                login(request, user)
                return redirect('home')

        except Exception as e:
            messages.error(request, 'An error has occured')

    context = {'login_form': login_form}
    return render(request, 'blog/login.html', context)


def profile_view(request):
    user = get_object_or_404(User, username=request.user)
    update_form = UserUpdateForm(instance=user)

    if request.method == 'POST':
        update_form = UserUpdateForm(request.POST, instance=user)

        if update_form.is_valid():
            update_form.save()
            messages.success(request, 'Profile details updated')
            return redirect('profile')
        
    context = {'update_form': update_form}
    return render(request, 'blog/profile.html', context)


def signout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

    context = {}
    return render(request, 'blog/logout.html', context)


class BlogPostsView(ListView):
    model = Post
    template_name = 'blog/posts.html'
    context_object_name = 'posts'


class BlogPostsDetailsView(DetailView):
    model = Post
    template_name = 'blog/posts_details.html'


class BlogPostsCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/posts_create.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogPostsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = BlogPostsForm
    template_name = 'blog/posts_create.html'
    success_url = reverse_lazy('posts')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class BlogPostsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/posts_delete.html'
    success_url = reverse_lazy('posts')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author




