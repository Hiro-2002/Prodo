from rest_framework import generics, permissions
from .models import Todo
from .serializers import TodoSerializer

class TodoListCreateView(generics.ListCreateAPIView):
    """
    - GET: List all todos for the logged-in user.
    - POST: Create a new todo for the logged-in user.
    """
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    - GET: Retrieve a single todo by ID for the logged-in user.
    - PUT/PATCH: Update the specified todo.
    - DELETE: Delete the specified todo.
    """
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)
