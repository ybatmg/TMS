from django.contrib import admin
from . models import TaskStage,Labels,Task,Attachments,Comments

# Register your models here.
admin.site.register(TaskStage)
admin.site.register(Labels)
admin.site.register(Task)
admin.site.register(Attachments)
admin.site.register(Comments)