from ..models import Employee
from django.db.models import F
from rest_framework import filters
from rest_framework.generics import GenericAPIView
from ..serializers.changepasswordSerializer import ChangePasswordSerializer
from rest_framework.response import Response
from rest_framework import status

class ChangePassword(GenericAPIView):
    serializer_class=ChangePasswordSerializer
    def post(self,request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            message=serializer.validated_data['message']
            #django_login(request, user)
            #token, created = Token.objects.get_or_create(user=user)
            return Response({"message":message}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)