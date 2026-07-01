from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from .filters import AeronaveFilter, _normalize
from .models import Aeronave
from .serializers import MatriculaSerializer, TipoVeiculoSerializer


class ApiRootView(APIView):
    """Lista os endpoints disponíveis na API."""

    def get(self, request, format=None):
        return Response(
            {
                "matriculas": reverse("matriculas", request=request, format=format),
                "filtros": reverse("filtros", request=request, format=format),
            }
        )


class MatriculasPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = "pageSize"
    max_page_size = 500


class MatriculasView(ListAPIView):
    serializer_class = MatriculaSerializer
    pagination_class = MatriculasPagination
    filterset_class = AeronaveFilter
    queryset = Aeronave.objects.all()

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        return (
            queryset.values("matricula", "fabricante").distinct().order_by("matricula")
        )


class FiltrosView(APIView):
    """Lista os filtros disponíveis para a MatriculasView."""

    def get(self, request):
        tipos_veiculo = sorted(
            {
                v.strip()
                for v in Aeronave.objects.values_list(
                    "tipo_veiculo", flat=True
                ).distinct()
                if v and v.strip()
            },
            key=_normalize,
        )

        serializer = TipoVeiculoSerializer(tipos_veiculo, many=True)
        return Response({"tiposAeronaves": serializer.data})
