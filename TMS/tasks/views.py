from django.shortcuts import render
from rest_framework import views
from . models import TaskStage,Labels,Task,Attachments,Comments
from . serializers import TaskStageSerializer,LabelsSerializer,TaskSerializer,AttachmentsSerializer,CommentsSerializer
from rest_framework.permissions import IsAuthenticated,BasePermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework import viewsets
from rest_framework.response import Response


# class IsOwnerrReadOnly(BasePermission):
   

#     def has_permission(self, request, view):

#         if request.user:
#                 return True

#         print(request.user.is_staff)

     
       

# Create your views here.
class TaskStageList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication,SessionAuthentication]
    queryset = TaskStage.objects.all()
    serializer_class = TaskStageSerializer

class LabelsList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]  
    queryset = Labels.objects.all()
    serializer_class = LabelsSerializer

class TaskList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    def create(self, request, *args, **kwargs):
        print(request.data)
        return super().create(request, *args, **kwargs)

    def list(self, request):
        queryset = Task.objects.all()
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)
    
class AttachmentsList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = Attachments.objects.all()
    serializer_class = AttachmentsSerializer

class CommentsList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer