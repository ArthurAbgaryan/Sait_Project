# -*- coding: utf-8 -*-

'''Урок №17 описание и изучение форм'''

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField
from pytils.translit import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Discussion(models.Model):
    title = models.CharField(max_length=100,
                            help_text='не более 100 символов',
                            db_index=True)
    content = RichTextField(max_length=2000, blank=True, null=True)
    date_create = models.DateTimeField(default=timezone.now)
    date_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100)
    likes_discussion = models.ManyToManyField(User, blank=True,
                                              related_name='discussion_likes',
                                              verbose_name='Лайкнувшие')
    saves_discussion = models.ManyToManyField(User, blank=True,
                                              related_name='blog_discussion_save',
                                              verbose_name='Сохранившие')
    reply = models.ForeignKey('self', null=True,
                              related_name='reply_ok_discussion',
                              on_delete=models.CASCADE)


    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Discussion,self).save(*args,**kwargs)

    def total_like(self):
        return self.likes_discussion.count()

    def total_saves_posts(self):
        return self.saves_discussion.count()

    class Meta:
        verbose_name='Дискусия'
        verbose_name_plural='Дискусии'

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse ('discussion_detail',kwargs={'pk':self.pk,'slug':self.slug})
# Create your models here.
