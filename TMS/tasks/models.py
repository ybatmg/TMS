from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class TaskStage(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

class Labels(models.Model):
    color = models.CharField(max_length=50)
    label = models.CharField(max_length=50)
    
    def __str__(self):
        return self.label
    
class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    cover = models.ImageField("taskcover",upload_to='taskcover/', null=True,blank=True)
    labels = models.ManyToManyField(Labels,related_name='labels')
    duedate = models.DateField(auto_now=True)
    stage = models.ForeignKey(TaskStage,on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True,null=True)
    assign_to = models.ManyToManyField(User,related_name='tasks_assigned_to')
    assign_by = models.ForeignKey(User,related_name='tasks_assigned_by',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name

class Attachments(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField("attachments",upload_to='attachments/',null=True,blank=True)
    size = models.CharField(max_length=200)
    task = models.ForeignKey(Task,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Comments(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    image = models.ImageField("comments",upload_to='comments/', null=True,blank=True)
    message = models.TextField()
    date = models.DateField(auto_now_add=True,null=True)
    task = models.ForeignKey(Task,null=True,on_delete=models.CASCADE)
    

    # def __str__(self):
    #     return self.name