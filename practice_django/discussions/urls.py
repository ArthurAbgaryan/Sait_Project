from django.urls import path
from .import views
from .views import DiscussionDetailView
#from .views import UserListView,PostCreateView,PostDetailView
urlpatterns = [

    #path('posts/user/<str:username>/',UserListView.as_view(),name='user-post-list'),
    path('create/',views.discussion_create,name='create'),
    path('discussion/<int:pk>/detail/<str:slug>/',DiscussionDetailView.as_view(),name='discussion_detail'),

    ]