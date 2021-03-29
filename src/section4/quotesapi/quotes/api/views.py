from django.views import generic
from rest_framework import generics as gn

from ..models import Quote
from .serializers import QuoteSerializer
from .permissions import IsAdminUserOrReadOnly
from .pagination import SmallSetPagination


class QuoteListCreateAPIView(gn.ListCreateAPIView):
    queryset = Quote.objects.all().order_by('id')
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = SmallSetPagination
