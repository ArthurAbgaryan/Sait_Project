## Описание views.py

## Вариант выборки с помощью get_queryset

```python

from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView
from .models import Post
from django.contrib.auth.models import User

class UserListView(ListView):
    model = Post
    #template_name = ''
    context_object_name ='blog_post_user_list'
    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_create')

```

template_name - имя шаблона html,которое мы задаем сами,если не задавать имя шаблона ,django автоматически будет его искать по имени "post_list

context_object_name - имя контекста позволяющее получитть данные из шаблона, то есть
это имя можно задавать самому. Есть базовые имена которыми можно воспользоваться,
это "object_list" и "имя модели с мал. буквы_list

get_queryset - переопределение метода, тут не используется метод super() т.к. идет обрашение
по конкретному полю, с помощью метода get_object_or_404

user=get_object_or_404(User,username=self.kwargs.get('username')):

Расписано в уроке №35

User,стандартная модель django

username- стандартное поле django 

self-обращение к памяти данных вызывающего,

kwargs-обрашение к словарю

get-метод получения по стандартному ключу(куда записывается логин при регистрации) значения username


## 2-ой выборки с помощью get_context_data

```python

    def get_context_data(self,**kwargs):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        context = super().get_context_data(**kwargs)
        queryset = Post.objects.filter(author=user)
        context['blog_post_user_list'] = queryset.order_by('-date_create')
        return context

```

user-переменная для выбора пользователя

сontext(Это словарь)-принимает значание функции от родительского класса

queryset-получаем выборку по фильтру и полученному user-у

Далее в словарь context,обычным методом которым добавляют в словари данные,добавляем новую выборку
        