
from django.urls import path
from .views import author_create, AuthorDetailView


urlpatterns = [

    #path('author/create/',AuthorCreateView.as_view(),name='author_create'),
    path('author/create/',author_create,name='author_create'),
    path('author/<int:pk>/detail/',AuthorDetailView.as_view(),name = 'author_detail')

]