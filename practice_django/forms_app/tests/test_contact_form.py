# -*- coding: utf-8 -*-

from forms_app.forms import ContactForm
import pytest
from django import forms
import datetime


'''
В декоратор передаем в виде строки поля нашей формы которые будут 
проверятся, и еше одну переменную для тестирования

Т.е. подготавливаем что тестируем и данные
'''
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
