from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, CreateView,DetailView
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


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



















