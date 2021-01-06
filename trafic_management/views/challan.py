from rest_framework import generics
from ..models import Challan
from ..serializer.challanSerializer import ChallanSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from mysite.filter import ChallanFilter
from rest_framework.response import Response
# from django_filters.rest_framework import DjangoFilterBackend
class ChallanView(generics.ListCreateAPIView):
    def get_queryset(self):
        return Challan.objects.filter(paidStatus=False).all()
    serializer_class=ChallanSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]
    # filter_class=ChallanFilter
    
    def list(self,request):
        queryset=self.get_queryset()
        officer=self.request.query_params.get('officer',None)
        paidStatus=self.request.query_params.get('paidStatus',None)
        plateNo=self.request.query_params.get('plateNo',None)
        if officer is not None:
            queryset=queryset.filter(officer=officer)
        if paidStatus is not None:
            queryset=queryset.filter(paidStatus__iexact=paidStatus.capitalize())
        if plateNo is not None:
            queryset=queryset.filter(plateNo__iexact=plateNo)
        # self.filter_class = ChallanFilter
        # print(self.filter_class)
        serializer=ChallanSerializer(queryset,many=True)
        return Response({"count":queryset.count(),"data":serializer.data})


class ChallanDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Challan.objects.all()
    serializer_class=ChallanSerializer

