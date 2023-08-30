from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, CreateView,DetailView,DeleteView,UpdateView
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy




def index(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'blog/index.html',context)

class UserListView(ListView):

    model = Post
    template_name = 'blog/user_posts.html'

    def get_context_data(self,**kwargs):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        context = super().get_context_data(**kwargs)
        queryset = Post.objects.filter(author=user)
        context['blog_post_user_list'] = queryset.order_by('-date_create')
        return context

class PostCreateView ( LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostDetailView(DetailView):
    model = Post
    #template_name = 'blog/post_detail.html'
    context_object_name = 'blog_post_detail'


    #LoginRequiredMixin -проверяет авторизован пользователь или нет
    #UserPassesTestMixin(стандартный миксин django) - проверяет права пользователя, в данном случае на статью
    #DetailView -удаляет
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin ,DeleteView):
    model = Post
    success_url = ('/')
    template_name = 'blog/post_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostUpdateView (LoginRequiredMixin, UserPassesTestMixin , UpdateView):
    model = Post
    fields = ['title','content'] #прописываем поля который будут редактироваться
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
















