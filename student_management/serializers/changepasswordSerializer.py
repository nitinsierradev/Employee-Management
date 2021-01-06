from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.core.mail import send_mail
from django.conf import settings
class ChangePasswordSerializer(serializers.Serializer):
    username=serializers.CharField( 
        write_only=True,
        required=True,
        style={'placeholder': 'username'},)
    newPassword=serializers.CharField( 
        write_only=True,
        required=True,
        style={'input_type': 'password', 'placeholder': 'newPassword'},)
    confirmPassword=serializers.CharField( 
        write_only=True,
        required=True,
        style={'input_type': 'password', 'placeholder': 'confirmPassword'},)

    def validate(self,data):
        user_obj=User.objects.get(username=data.get('username'))
        newPassword=data.get('newPassword',None)
        confirmPassword=data.get('confirmPassword',None)
        if (confirmPassword!=newPassword):
            raise serializers.ValidationError(
                'confirm password is same as oldpassword'
                )
        if(newPassword==confirmPassword):
            user_obj.set_password(newPassword)
            user_obj.save()
            data['message']='Password Updated Sucessfuly'
            send_mail('Change Password','Your Password has changed',settings.EMAIL_HOST_USER,['sumittarwey2268@gmail.com'],fail_silently=False)
        return data
        
        
