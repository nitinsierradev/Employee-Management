from rest_framework import serializers
from ..models import RankingCreteria

class RankingCreteriaSerializer(serializers.ModelSerializer):

    class Meta:
        fields  = '__all__'
        model   = RankingCreteria