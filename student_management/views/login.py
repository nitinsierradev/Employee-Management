from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from ..serializers.loginSerializer import LoginSerializer
from ..serializers.employeeSerializer import EmployeeSerializer
from rest_framework import status
from django.contrib.auth import login as django_login
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from ..models import Employee
class LoginApiView(GenericAPIView):
    authentication_classes=()
    permission_classes=()
    serializer_class=LoginSerializer
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            django_login(request, user)
            print(request.user)
            token_object=Token.objects.filter(user=user)
            # print(token_object)
            if token_object:
                request.user.auth_token.delete()
            token = Token.objects.create(user=user)
            checkEmployee = Employee.objects.get(user=user.id)
            EmployeeObj = get_object_or_404(Employee,pk=checkEmployee.id)
            employeeData = EmployeeSerializer(EmployeeObj)
            employeeDetail=employeeData.data
            del employeeDetail['id']
            # print(employeeDetail)
            return Response({"token":token.key,"userDetail":employeeDetail}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Logout(APIView):
    def get(self, request, format=None):
        print(request.user)
        request.user.auth_token.delete()
        logout(request)
        # Token.objects.filter(id=request.user.id).delete()
        # simply delete the token to force a login
        return Response(status=status.HTTP_200_OK)