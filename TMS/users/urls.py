from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('users',views.UserView,basename="users")

urlpatterns = [
    # path('signup/',views.signup_view,name="signup"),
    path('token/',TokenObtainPairView.as_view(),name="token_obtain_pair"),
    path('token/refresh/',TokenRefreshView.as_view(),name="token_resfresh"),
    path('token/verify/',TokenVerifyView.as_view(),name="token_verify"),
    path('view/',include(router.urls))
]

