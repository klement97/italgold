from django.contrib.auth.models import User
from django.urls import path
from rest_framework.generics import ListAPIView
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserListAPIView(ListAPIView):
    queryset = User.objects.order_by('id')
    serializer_class = UserSerializer


urlpatterns = [
    path('user/', UserListAPIView.as_view())
    ]
