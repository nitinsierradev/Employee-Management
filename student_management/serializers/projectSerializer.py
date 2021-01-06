from rest_framework import serializers
from ..models import Project

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        fields  = '__all__'
        model   = Project