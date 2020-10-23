from . import views

from django.urls import path, include
from django.views.generic import TemplateView

from rest_framework_simplejwt.views import TokenRefreshView

app_name = 'myapp'

urlpatterns = [
    path('', TemplateView.as_view(template_name='myapp/index.html')),
    path('api/register', views.UserRegisterView.as_view(), name='user-register'),
    path('api/login', views.UserLoginView.as_view(), name='user-login'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
