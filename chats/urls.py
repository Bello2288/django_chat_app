from django.urls import path

from .views import ChatListAPIView, MessageListAPIView, MessageDetailAPIView

urlpatterns = [
    # path('reviews/', ReviewListCreateAPIView.as_view()),
    # path('books/', BookListAPIView.as_view())

    path('messages/<int:pk>/', MessageDetailAPIView.as_view()),
    # path('reviews/', ReviewListAPIView.as_view()),
    path('books/<int:chat>/messages/', MessageListAPIView.as_view()),
    path('chats/', ChatListAPIView.as_view()),

]