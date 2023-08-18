# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from .forms  import ContactForm
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.utils.encoding import force_str

from django.http import HttpResponse,request
from django.views.generic import DetailView
from blog.models import Post
import datetime

def contact_send(request):
    if request.method == "GET": #если пользователь перешел по ссылке(т.е. Get -запрос)то перенаправить на пустую форму
        form = ContactForm()
    else:
        form = ContactForm(request.POST,request.FILES)
        if form.is_valid():
            #date_created = form.cleaned_data['date_created']
            '''
            if date_created < datetime.date.today():
                form = ContactForm()
                messages.error(request,'Введите корректную дату ')
                form = ContactForm()
                return render(request, 'forms_app/email.html', {'form': form})
            '''
            subject = form.cleaned_data['subject']
            message =form.cleaned_data['message']

            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
            recipients = ['abgaryanarthurelina@gmail.com']

            if cc_myself:
                recipients.append(subject)
                recipients.append(message)
            try:
                send_mail(subject, message, sender, recipients)
            except BadHeaderError:
                return HttpResponse("Не правильно введенный формат")
            #return redirect('success')
            form = ContactForm()
            messages.success(request,'SUCCESS')#это фу-ия вместо предыдущей, выводиться сообщ. вместо перенаправления
        else:
            messages.error(request,'Error') #Если is_valid не проходит условие, то выводиться сообщение об ошибке

    return render (request, 'forms_app/email.html', {'form':form})
#def send_success(request):
    #return HttpResponse('Ваше сообшение доставлено')
