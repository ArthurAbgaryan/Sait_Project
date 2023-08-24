# -*- coding: utf-8 -*-

from forms_app.forms import ContactForm
import pytest
from django import forms
import datetime
max_length_gt_100 = 'n'*101
max_length_gt_99 = 'n'*99



@pytest.mark.parametrize(
    #тестируем только поле date_created, и присваиваем ему значение date_valid = True
    #здесь вводятся различные параметры для проверки этого поля
    'date_created,date_created_valid',[
        (datetime.date.today(),True),#чтобы постоянной не менть дату , можно вставить модкль datetime.date.today()
        ('2023-08-16',True),#не верные данные при которых тест должен выдать ошибку, после умпешной проверки ставим FALSE
        ('2023-08-18',True),
        ('',False),#ставим значение "пустая строка", что недопустимо. Т к по документации это не допустимо, можно ток None

    ]
)


@pytest.mark.parametrize(
    #этот вариант заполнения истины, поэтому значение subject_valid = True
    'subject,subject_valid',[
        ('django',True),
        (max_length_gt_100,False),#тест работает, проверка на максимум сиволов
        (max_length_gt_99, True),#тест работает , проверка на допустимое количество символов
        ('',False),#тест прошел так как поле не может быть пустым, т.к. в поле есть флажок required = True
    ]
)

@pytest.mark.parametrize(
    'message,message_valid',[
        ('My name is Arthur',True),
        #(),
        #(),
    ]
)

@pytest.mark.parametrize(
    'sender,sender_valid',[
        ('django@mail.ru',True),
        #(),
        #(),
    ]
)

@pytest.mark.parametrize(
    #Так как этот аргумент является булевым вырожением,то как параметр передается сам аргумент
    'cc_myself,cc_myself_valid',[
        ('cc_myself',True),
        #(),
        #(),
    ]
)

def test_contact_form(date_created,subject,message, sender ,cc_myself,
                      date_created_valid,subject_valid,message_valid,sender_valid,cc_myself_valid):
    form = ContactForm (
        data = {
            'date_created':date_created,
            'subject':subject,
            'message':message,
            'sender':sender,
            'cc_myself':cc_myself,
        }
    )
    f = form.errors.as_data()
    print(f)
    assert form.is_valid() is (date_created_valid and subject_valid  and message_valid and sender_valid and cc_myself_valid)

'''

В декоратор передаем в виде строки поля нашей формы которые будут 
проверятся, и еше одну переменную для тестирования

Т.е. подготавливаем что тестируем и данные

@pytest.mark.parametrize(
    'date_created,subject,message, sender ,cc_myself,validity', [
        #это рабочий вариант
        ('2023-08-14', 'django', 'Hi , My name is Arthur', 'django@mail.ru', 'cc_myself', True),
        #меняем дату
        ('2023-08-20', 'django', 'Hi , My name is Arthur', 'django@mail.ru', 'cc_myself', True),

        #неправильный e-mail
        ('2023-08-20', 'django', 'Hi , My name is Arthur', 'djangomail.ru', 'cc_myself', True)
    ]
)

def test_valid_contact_form(date_created,subject,message, sender ,cc_myself,validity):
    #создаем словарь для передачи данных(для понятности ключ и значение по названию совпадают)
    form = ContactForm (
        data = {
                'date_created': date_created,
                'subject': subject,
                'message': message,
                'sender': sender,
                'cc_myself': cc_myself
                }
    )
    f = form.errors.as_data()
    print (f)
    assert form.is_valid() is validity
'''