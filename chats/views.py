from rest_framework import generics

from .models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.


class ChatListAPIView(generics.ListAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class MessageListAPIView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        chat = self.kwargs['chat']
        return Message.objects.filter(chat=chat)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class MessageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsAuthorOrReadOnly,)
