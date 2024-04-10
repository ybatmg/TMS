from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model
from . models import Work

User=get_user_model()

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    work = serializers.SerializerMethodField('get_works')
    class Meta:
        model = User
        fields = '__all__'
    def get_works(self,obj):
        worklist = []
        if obj:
            works = Work.objects.filter(user=obj)

            for work in works:
                worklist.append(work.title)
        return worklist