

from django.urls import path
from .views import UserListView,PostCreateView,PostDetailView
urlpatterns = [

    path('posts/user/<str:username>/',UserListView.as_view(),name='user-post-list'),
    path('post/new/',PostCreateView.as_view(),name='post_create'),
    path('post/<int:pk>/detail/<str:slug>/',PostDetailView.as_view(),name='post_detail'),

    ]