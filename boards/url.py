from django.urls import path
from . import views
urlpatterns = [
    path('',views.BoardListView.as_view(),name='boards'),
    path('about/',views.about,name='about'),
    path('boards/<int:board_id>/', views.board_topics, name='topics'),
    path('boards/<int:board_id>/new/', views.new_topic, name='new_topic'),
    path('boards/<int:board_id>/topics/<int:topic_id>/', views.topic_posts, name='topic_posts'),
    path('boards/<int:board_id>/topics/<int:topic_id>/reply/', views.reply_for_topic, name='reply_for_topic'),
    path('boards/<int:board_id>/topics/<int:topic_id>/post/<int:post_id>/edit/', views.PostUpdateView.as_view(), name='edit_post'),
]
