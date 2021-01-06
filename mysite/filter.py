import django_filters
from trafic_management.models import Challan
class ChallanFilter(django_filters.FilterSet):
    paidStatus = django_filters.BooleanFilter(lookup_expr='exact')
    plateNo    = django_filters.CharFilter(lookup_expr='iexact')
    officer    = django_filters.NumberFilter(field_name='officer')

    class Meta:
        model = Challan
        fields = ['paidStatus', 'plateNo','officer']
