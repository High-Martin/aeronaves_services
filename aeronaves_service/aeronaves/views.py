from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from .filters import AeronaveFilter
from .models import Aeronave
from .serializers import MatriculaSerializer


class MatriculasPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'pageSize'
    max_page_size = 500


class MatriculasView(ListAPIView):
    serializer_class = MatriculaSerializer
    pagination_class = MatriculasPagination
    filterset_class = AeronaveFilter
    queryset = Aeronave.objects.all()

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        return queryset.values('matricula', 'fabricante').distinct().order_by('matricula')
