from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from . models import TaskStage,Labels,Task,Attachments,Comments
from users.serializers import UserSerializer
User = get_user_model()

class LabelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Labels
        fields = '__all__'

class AttachmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachments
        fields = '__all__'

class CommentsSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField('get_user')
    class Meta:
        model = Comments
        fields = '__all__'
    def get_user(self, obj):
        name = None
        if obj.user_id:
            name = obj.user_id.username  # Assuming 'username' is the field you want to retrieve       
        return name
    
class TaskSerializer(serializers.ModelSerializer):
    labels = LabelsSerializer(many =True,read_only = True)
    attachments = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    class Meta:
        model = Task
        fields = '__all__'
    # get comments
    def get_comments(self, obj):
        comments = Comments.objects.filter(task=obj)
        return CommentsSerializer(comments, many=True).data
    # get attachments
    def get_attachments(self, obj):
        attachments = Attachments.objects.filter(task=obj)
        return AttachmentsSerializer(attachments, many=True).data
    

class TaskStageSerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField(read_only = True)
    class Meta:
       model = TaskStage
       fields = '__all__'

    def get_tasks(self, obj):
        task = Task.objects.filter(stage=obj)
        return TaskSerializer(task, many = True).data
