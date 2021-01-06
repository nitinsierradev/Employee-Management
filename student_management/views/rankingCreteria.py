from ..models import RankingCreteria
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..serializers.rankingCreteriaSerializer import RankingCreteriaSerializer
from rest_framework.generics import GenericAPIView

class RankingCreateriaList(GenericAPIView):
    serializer_class = RankingCreteriaSerializer
    queryset = RankingCreteria.objects.all()
    def get(self, request, format=None):
        print(request.user)
        print(request.user.is_authenticated)
        rankingCreteria = RankingCreteria.objects.all()
        serializer = RankingCreteriaSerializer(rankingCreteria, many=True)
        return Response(serializer.data)
    def post(self,request,format=None):
        serializer = RankingCreteriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RankingCreateriaShow(GenericAPIView):
    serializer_class = RankingCreteriaSerializer
    def get(self, request, pk, *args, **kwargs):
        rankingCreteria = get_object_or_404(RankingCreteria,pk=pk)
        serializer = RankingCreteriaSerializer(rankingCreteria)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        rankingCreteria = get_object_or_404(RankingCreteria, pk=pk)
        serializer = RankingCreteriaSerializer(rankingCreteria, data=request.data, partial=True)
        if serializer.is_valid():
            rankingCreteria = serializer.save()
            return Response(RankingCreteriaSerializer(rankingCreteria).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        rankingcreteria = get_object_or_404(RankingCreteria, pk=pk)
        rankingcreteria.delete()
        return Response("Ranking Creteria deleted", status=status.HTTP_204_NO_CONTENT)
        
