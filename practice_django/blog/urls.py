

from django.urls import path
from .views import UserListView,PostCreateView,PostDetailView,PostDeleteView, PostUpdateView
from .views import index
urlpatterns = [
    path('',index, name = 'index_home'),
    path('posts/user/<str:username>/',UserListView.as_view(),name='user-post-list'),
    path('post/new/',PostCreateView.as_view(),name='post_create'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name = 'post_delete'),
    path('post/<int:pk>/detail/<str:slug>/',PostDetailView,name='post_detail'),
    #path('post/<int:pk>/detail/<str:slug>/',PostDetailView.as_view(),name='post_detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(),name ='post_update'),

    ]