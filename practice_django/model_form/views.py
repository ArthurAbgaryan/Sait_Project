# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Author

from .forms import AuthorForm

#model_form/author/create/
def author_create(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            create_author = form.cleaned_data
            create_author = form.save()
            create_author.save()

            '''
            name = form.cleaned_data['name']
            title = form.cleaned_data['title']
            birth_day = form.cleaned_data['birth_day']
            '''

            return redirect(create_author.get_absolute_url())

    else:
        form = AuthorForm()

    return render(request, "model_form/author_form.html", {"form": form})

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'model_form/author_detail.html/'


# Create your views here.
