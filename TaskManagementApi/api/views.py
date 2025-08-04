from rest_framework import generics
from .models import Project, Task, Comment
from .serializers import ProjectSerializer,TaskSerializer,CommentSerializer
# Create your views here.

class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer



class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset= Project.objects.all()
    serializer_class = ProjectSerializer



class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer



class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset= Task.objects.all()
    serializer_class = TaskSerializer


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer



class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset= Comment.objects.all()
    serializer_class = CommentSerializer
