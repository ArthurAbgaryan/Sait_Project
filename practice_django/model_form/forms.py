from django import forms
from django.forms import ModelForm, Textarea
from .models import Author, Book
from django import forms
from .models import TITLE_CHOICES


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        widgets = {
            'name':Textarea(attrs = {'cols':80,'rows':20})
        }
        labels = {
            'name':('Описание')
        }
        help_texts = {
            'name':('введите аккуратно')
        }
        error_messages = {
            'name':{
                'max_length':('введите не более 100 символов')
            }
        }



"""
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

    name = forms.CharField(max_length =100)
    title = forms.CharField(max_length=3, widget=forms.Select(choices=TITLE_CHOICES))
    birth_day = forms.DateField(required=False)

class BookForm(forms.Form):
    name = forms.CharField(max_length=100)
    author = forms.ModelMultipleChoiceField(queryset=Author.objects.all())



'''class AuthorForm(ModelForm):
    model = Author
    fields = ['name','title','birth_day']

class BookForm(ModelForm):
    model = Book
    fields = ['name','author']
'''
"""