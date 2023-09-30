

from django.urls import path
from .views import UserListView,PostCreateView,PostDeleteView, PostUpdateView, HomePostListViewAllUsers
from .views import index,post_detail_view, all_save_view_posts,save_post_is_ajax
urlpatterns = [
    path('',index, name = 'index_home'),
    path('posts/user/<str:username>/',UserListView.as_view(),name='user-post-list'),
    path('post/new/',PostCreateView.as_view(),name='post_create'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name = 'post_delete'),
    path('post/<int:pk>/detail/<str:slug>/',post_detail_view,name='post_detail'),
    #path('post/<int:pk>/detail/<str:slug>/',PostDetailView.as_view(),name='post_detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(),name ='post_update'),
    path('home/',HomePostListViewAllUsers.as_view(),name = 'blog_home'),
    path('saved_posts/', all_save_view_posts, name='all_save'),
    path('post/save/', save_post_is_ajax, name='post_save'),

]