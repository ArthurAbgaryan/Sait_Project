from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, CreateView,DetailView,DeleteView,UpdateView
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
import random
from .forms import CommentForm
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, JsonResponse



'''!!!!!Титульная страница, все сделано'''
def index(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'blog/index.html',context)


'''!!!Написать вывод всех постов'''
class HomePostListViewAllUsers(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'all_posts'
    ordering = ['-date_create'] #сортировка в обратном порядке
    paginate_by = 3
    def get_context_data(self, *args, **kwargs): #будет добавлять рондомный список с именем "random"
        context = super(HomePostListViewAllUsers,self).get_context_data() #применение метода к род-ому классу PostListView, т.е получаем список из класса PostListView
        users = list(User.objects.exclude(pk = self.request.user.pk)) #получаем пол-ей без pk
        if len(users) > 3: #если пол-ей меньше 3
            out = 3
        else:
            out = len(users) #кол-во пол-ей
        random_user = random.sample(users, out) #рандомное размешение юзеров
        context['random'] = random_user
        return context





class UserListView(ListView):

    model = Post
    template_name = 'blog/user_posts.html'


    context_object_name = 'blog_post_user_list'
    paginate_by = 2 #указ-ся сколько страниц отображает пагинация
    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(author=user)

'''
    def get_context_data(self,**kwargs):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        context = super().get_context_data(**kwargs)
        queryset = Post.objects.filter(author=user)
        context['blog_post_user_list'] = queryset.order_by('-date_create')
        return context
'''

class PostCreateView ( LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)


'''
class PostDetailView(DetailView):
    model = Post
    #template_name = 'blog/post_detail.html'
    context_object_name = 'blog_post_detail'
'''

def post_detail_view(request, pk, slug):#обязательный параметр request(как в фу-ях)
    #как обрабатывать
    handle_page = get_object_or_404(Post, id=pk, slug= slug)#получ. объект из Post, по id и slug
    total_comment = handle_page.comments_blog.all().filter(replay_comment=None).order_by('-id') #выводим коментрии,без поля replay_comment
    total_comment2 = handle_page.comments_blog.all().order_by('-id')
    total_likes = handle_page.total_likes() #вызвваем мет. подсчета лайков к нашему посту, из модели
    total_save = handle_page.total_saves_posts()#вызвваем мет. подсчета сохраненных постов, из модели

    #что извлечь
    context = {}

    if request.method == 'POST':
        comments_qs = None
        comments_form = CommentForm(request.POST or None)
        if comments_form.is_valid():
            form = request.POST.get('body') #получаем данные с поля 'body'
            comment = Comment.objects.create( #создаем обьект класса Comment
                              post = handle_page, #полю присваивается выше полученный обьект
                              name_author = request.user, #полю автора запрашиваем пользователя
                              body = form, #этому полю присваивается выше полученный form
                              replay_comment = comments_qs ) #так как коммент созд без ответа на него, то присв. None
            comment.save()#сохраняем
    else:
        comments_form = CommentForm()
    context['comments_form'] = comments_form
    context['comments'] = total_comment
    context['post_cn'] = handle_page

    if request.is_ajax():
        html = render_to_string('blog/comments.html',context) #подгружаем шаблон коментариев
        return JsonResponse({'form':html})# пер-ся ключ form , котор. ранее получили, и значение html

    return render (request, 'blog/post_detail.html', context)




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
















