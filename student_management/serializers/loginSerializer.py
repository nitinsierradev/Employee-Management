from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
class LoginSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=100,write_only=True,required=True,help_text='username')
    password=serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'},
    )

    def validate(self,data):
        username=data.get('username',None)
        password=data.get('password',None)

        if username and password is not None:
            user=authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    data['user']=user
            else:
                raise serializers.ValidationError(
                'user with this account is not exits'
                )

        else:
            raise serializers.ValidationError(
                'Enter Valid username or password'
            )
        return data