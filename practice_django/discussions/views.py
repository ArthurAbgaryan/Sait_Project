from django.shortcuts import render
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView, CreateView,DetailView
from .models import Discussion
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
'''Урок №20'''
from django.contrib.auth.decorators import login_required #декоратор который разрешает заполнять форму только
                                                          #зарегистрированным пользователям
from .forms import DiscussionCreateForm
from django.contrib import messages #мини фрейм форк для выведения сообшений пользователю урок 25


class UserDiscussionListView(ListView):

    model = Discussion
    template_name = 'discussion/user_discussion.html'

    def get_context_data(self,**kwargs):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        context = super().get_context_data(**kwargs)
        queryset = Discussion.objects.filter(author=user)
        context['discussion_post_user_list'] = queryset.order_by('-date_create')
        return context


class DiscussionDetailView(DetailView):
    model = Discussion
    template_name = 'discussions/discussion_detail.html'
    context_object_name = 'discussion_detail'

@login_required #урок 20
def discussion_create(request): #в представлениях в фун-ии всегда передается request, т.е. в web всегда идет
                                #http запрос, в классах это скрыто от нас
    if request.method == "POST":  #первое что нужно проверять при создании формы, имеет ли запрос метод Post другого запросы в формы и не должно быть
        #создадим экземпляр формы и заполним его данными запроса
        #Создадим форму для редактирования
        #Т.Е. джанго переменной form формирует с помошью данных из forms.py форму для заполнения
        form = DiscussionCreateForm(request.POST, request.FILES) #Данные POST для заполнения формы, request.POST формирует html форму
        if form.is_valid:
            new_discussion = form.save(commit=False)#commit = False позволяет сохранять форму до нажатия кнопки
                                                    #то есть сохранение происходит в оперативной памяти
            new_discussion.author = request.user # определяет кто заполняте поле, тоесть выбираем поле модели и далее делаем запрос
            new_discussion.save()#это уже метод сохранения  в БАЗЕ ДАННЫХ
            messages.success(request,'Cтатья успешно добавлена')#сообшение добаляется после успешного сохранения статьи урок 25
            return redirect(new_discussion.get_absolute_url()) #перенаправление после сохранения
    else: #если приходит GET или другой запрос, то откроется пустая форма form = DiacussionCreateForm()
         #это форма открывается при переъоде по ссылке, но в итоге вполняется верхний блок так как нач. заполнение
        form = DiscussionCreateForm()

    return render(request, 'discussions/create_form.html',{'form':form})

