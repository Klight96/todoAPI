from rest_framework import generics

from .models import Todo
from .serializers import TodoSerializer


class ListTodo(generics.ListAPIView):
  queryset = Todo.object.all()
  serializer_class = TodoSerializer


class DetailTodo(generics.DetailAPIView):
  queryset = Todo.object.all()
  serializer_class = TodoSerializer




