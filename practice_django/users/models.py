#-*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model): #соз-ли модель, которая фактически явл-ся дополнением к стна-ой модели User
    user = models.OneToOneField(User,on_delete = models.CASCADE)#поле которое расширяет модель User
    is_online = models.BooleanField(default = False)# поле определяющее онлайн профиля
    following = models.ManyToManyField(User, related_name = "folowing", blank = True) #поле описывающее кто следит за профилем
    friends = models.ManyToManyField(User,related_name = 'my_friends', blank = True)#поле друзей
    bio = models.CharField(max_length = 150, blank = True)#поле заполнения о себе
    date_birthd = models.CharField(max_length=10, blank=True)#дата рождения
    created = models.DateTimeField(auto_now_add=True) #дата создания профиля
    update = models.DateTimeField(auto_now=True)#обновления
    image = models.ImageField(default = 'default_profile.png',upload_to= 'profiles_img' ,blank=True)#картинка профиля

    def profile_posts(self):
        """
               чтобы установить связь между пользователем и постом,
                напишите связанное имя модели в маленьком регистре,
                а затем используйте _set.
                fields.name_model_relation + _set.metod()
        """
        return self.user.post_set.all()


    def get_friends(self): #метод получение всех друзей
        return self.friends.all()

    def get_friends_no(self):#подсчет друзей
        return self.friends.all().count()

    def __str__(self): #возврашает имя пользователя через класс User
        return f'{self.user.username} Profile'

'''выборка статуса, обязательно с большой буквы'''
STATUS_CHOICES = (
    ('send','send'),
    ('accepted','accepted')
)
class Relationship(models.Model): #модель для отправки завки в друзья
    sender = models.ForeignKey(Profile, on_delete = models.CASCADE,
                               related_name='friend_sender')
    receiver = models.ForeignKey(Profile, on_delete = models.CASCADE,
                               related_name = 'friend_receiver')
    status = models.CharField(max_length = 10, choices = STATUS_CHOICES) #статус который выбирается из созданной нами выборки
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.sender}-{self.receiver}-{self.status}'


# Create your models here.
