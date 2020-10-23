import requests
from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.permissions import AllowAny

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .serializers import UserRegisterSerializer
from .models import UserLoginHistory


class UserRegisterView(generics.CreateAPIView):
    """
    User Registration View
    """
    model = User
    serializer_class = UserRegisterSerializer
    permission_classes = (AllowAny,)


class UserLoginView(TokenObtainPairView):
    """
    User Login View
    """
    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        user = User.objects.get(username=username)
        ip_address = get_client_ip(request)

        # Save login history record
        UserLoginHistory.objects.create(user=user, ip=ip_address)
        
        # Send webhook to team
        uri = "https://encrusxqoan0b.x.pipedream.net/"
        payload = {
            "user": user.id,
            "ip": ip_address,
        }
        response = requests.post(uri, data=payload)

        return super(UserLoginView, self).post(request, *args, **kwargs)


def get_client_ip(request):
    """
    Return IP address of client
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
