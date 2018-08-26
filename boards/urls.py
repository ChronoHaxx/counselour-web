from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.BoardListView, name='home'),
    path('boards/<pk>/', views.TopicListView, name='board_topics'),
    path('boards/<pk>/new/', views.new_topic, name='new_topic'),
    path('boards/<pk>/topics/<topic_pk>/', views.PostListView, name='topic_posts'),
    path('boards/<pk>/topics/<topic_pk>/reply/', views.reply_topic, name='reply_topic'),
    path('boards/<pk>/topics/<topic_pk>/posts/<post_pk>/edit/',
        views.PostUpdateView, name='edit_post'),
]
