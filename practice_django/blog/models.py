from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField #импортирование текстового редактора из библиотеки ckeditor
#from django.utils.text import slugify #при импорте с джанго русские буквы могут не работать
from pytils.translit import slugify #импорт той же функции только со сторонней библиотеки
#from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save #импорт сигнала pre_save(т.е. сохран. до создания) (урок 14-15)
from django.dispatch import receiver #импорт декоратора (урок 14-15)




class Post(models.Model):

    class Meta:
        verbose_name='Создание поста'
        verbose_name_plural='Создание постов'

    def __str__(self):
        return self.title

    '''db_index позволяет быстрее производить поиск по данному поля, 
    при большом количестве эл-ов'''
    title=models.CharField(max_length=200, db_index=True)
    #content=models.TextField(max_length=2000,blank=True, null=True)

    '''
    применение ckeditor(текстовый редактор)
    так как он не имеет обшего с .models то прописываем без .models
    https://django-ckeditor.readthedocs.io/en/latest/
    '''
    content=RichTextField(max_length=2000,blank=True, null=True)

    date_create=models.DateTimeField(default=timezone.now)
    date_update=models.DateTimeField(auto_now=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)# null=True если анонимный пользовател
    slug=models.SlugField(max_length=100)#unique=True
    likes_post=models.ManyToManyField(User,blank=True,related_name='post_likes',verbose_name='Лайкнувшие')# описание поля лайков
    saves_posts=models.ManyToManyField(User, blank=True,related_name='blog_posts_save',verbose_name='Сохранившие')
    reply=models.ForeignKey('self',null=True,related_name='reply_ok',on_delete=models.CASCADE)

    def total_likes(self):
        return self.likes_post.count()

    def total_saves_posts(self):
        return self.saves_posts.count()

    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk,'slug':self.slug})

'''

def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Post,self).save(*args,**kwargs)

'''


#https://docs.djangoproject.com/en/4.2/topics/signals/
@receiver(pre_save,sender=Post)
def prepopulated_slug(sender,instance,**kwargs):
    instance.slug=slugify(instance.title)




'''Модель коментариев'''

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments_blog')
    name_author = models.ForeignKey(User, on_delete = models.CASCADE) #django само создает related_name ,еслт его не указывать
    body = models.TextField(max_length = 255)
    date_created = models.DateTimeField(auto_now_add = True)
    likes_comment = models.ManyToManyField(User,related_name = 'likes_blog_comment', blank = True)
    replay_comment = models.ForeignKey('self' , null = True, related_name='replay_blog_comment', on_delete = models.CASCADE)

    def __str__(self):
        return "%s - %s - %s" %(self.post.title, self.name_author, self.id)
    def total_likes_comment(self):
        return self.likes_comment.count()

    def get_absolute_url(self):
        return reverse ('post_detail',kwargs = {'pk':self.pk})
