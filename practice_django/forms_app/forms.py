#-*- coding : utf-8 -*-

from django import forms
import datetime

class ContactForm(forms.Form):
    date_created = forms.DateField (initial = datetime.date.today, required=True, help_text = "Заполнить не позднее 1-ой недели")#init-как
    #мы расматривали в предыдущих уроках автоматический заполняет поле, inittial -это аргумент поля формы
    #аргумент required = False означает что поле может быть не заполнено
    subject = forms.CharField(label = 'Введите заголовок',max_length = 100)
    message = forms.CharField (max_length = 500)
    sender = forms.EmailField ()
    cc_myself = forms.BooleanField(required=True) #Есди указали это поле то оно обязательное,
                                                    #если поле необязательно то нужно  указывать required=False

    def clean_date_creation(self):
        data = self.cleaned_data['date_created']
        if data < datetime.date.today():
            raise forms.ValidationError(('Дата отправки не верна'))
        return data
