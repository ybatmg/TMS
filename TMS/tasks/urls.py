from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . views import TaskList,TaskStageList,LabelsList,AttachmentsList,CommentsList


router = DefaultRouter()
router.register('task',TaskList,basename='tasklist')
router.register('taskstage',TaskStageList,basename='taskstage')
router.register('labels',LabelsList,basename='labels')
router.register('attachments',AttachmentsList,basename='attachments')
router.register('comments',CommentsList,basename='comments')



urlpatterns = [
    path('',include(router.urls))
]
