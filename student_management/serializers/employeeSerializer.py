from rest_framework import serializers
from ..models import Employee,EmployeeProjectLog
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
class EmployeeSerializer(serializers.ModelSerializer):
    #name=serializers.SerializerMethodField()
    password = serializers.CharField(
        write_only=True,
        required=False,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    reportingEmployeeName=serializers.CharField(read_only=True)
    projectName=serializers.CharField(read_only=True)

    class Meta:
        fields  = '__all__'
        model   = Employee
    def create(self, validated_data):
        # logger.info("Employee Created SuccessFully")
        password=validated_data.pop('password')
        user=User.objects.create_user(first_name=validated_data['firstName'],last_name=validated_data['lastName'],email=validated_data['email'],username=validated_data['email'],password=password)
        validated_data['user']=user
        employee=Employee.objects.create(**validated_data)
        return employee
    def update(self, instance, validated_data):
        user=User.objects.get(pk=instance.id)
        user.first_name = validated_data['firstName']
        user.last_name  = validated_data['lastName']
        user.email      = validated_data['email']
        user.username   = validated_data['email']
        user.is_active  = validated_data['is_active']
        user.save()
        instance.firstName = validated_data.get('firstName',instance.firstName)
        instance.lastName = validated_data.get('lastName',instance.lastName)
        instance.email = validated_data.get('email',instance.email)
        instance.dob = validated_data.get('dob',instance.dob)
        instance.is_active = validated_data.get('is_active',instance.is_active)
        instance.mobileNo = validated_data.get('mobileNo',instance.mobileNo)
        instance.reportingEmployee=validated_data.get('reportingEmployee',instance.reportingEmployee)
        instance.empId    = validated_data.get('empId',instance.empId)
        if instance.project.id!=validated_data['project'].id:
            EmployeeProjectLog.objects.create(employee=instance,project=validated_data['project'])
        instance.project=validated_data.get('project',instance.project)
        instance.save()
        return instance


