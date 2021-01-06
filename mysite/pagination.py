from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination
from django.db.models import Avg

class ListLimitoffsetPagination(LimitOffsetPagination):
    max_limit=10
    default_limit=3

class PaginationWithAggregates(LimitOffsetPagination):
    def paginate_queryset(self, queryset, request, view=None):
        self.avg_rating = queryset.aggregate(avg_rating=Avg('rating'))['avg_rating']
        return super(PaginationWithAggregates, self).paginate_queryset(queryset, request, view)

    def get_paginated_response(self, data):
        paginated_response = super(PaginationWithAggregates, self).get_paginated_response(data)
        paginated_response.data['avg_rating'] = self.avg_rating
        return paginated_response
    max_limit=10
    default_limit=5