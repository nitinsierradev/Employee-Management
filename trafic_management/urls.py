from django.conf.urls import url,include
from .views import challan
urlpatterns = [
    url(r'list/$', challan.ChallanView.as_view(), name='challanList'),
    url(r'show/(?P<pk>\d+)/$',challan.ChallanDetailView.as_view(), name='challanDetail'),
]