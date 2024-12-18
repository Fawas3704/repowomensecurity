from rest_framework import serializers

from securityapp.models import *
from rest_framework.serializers import ModelSerializer


class FriendlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendTable
        fields = ['id','user_id', 'friend_name', 'friend_no']

# class FriendlistViewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Friendlist
#         fields = ['user_id', 'friend_name', 'friend_no']

class FriendlistEditSerializer(ModelSerializer):
    class Meta:
        model = FriendTable
        fields = ['friend_name', 'friend_no']


class UserSerializer(ModelSerializer):
    class Meta:
        model=UserTable
        fields=['LOgin','Firstname','Lastname','Age','place','post','pin','number','Email']

class LoginSerializer(ModelSerializer):
    class Meta:
        model=LoginTable
        fields=['Username','Password']