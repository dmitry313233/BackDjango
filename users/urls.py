from django.urls import path

from .apps import UsersConfig
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from .views import UserRegisterView

app_name = UsersConfig.name

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('registration/', UserRegisterView.as_view(), name='registration'),
]
