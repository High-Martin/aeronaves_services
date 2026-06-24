from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from .models import Aeronave
from .serializers import AeronaveDetailSerializer


class ApiRootView(APIView):
    """Lista os endpoints disponíveis na API."""

    def get(self, request, format=None):
        return Response({
            'aeronave-detail': reverse(
                'aeronave-detail',
                kwargs={'matricula': 'PTPFO'},
                request=request,
                format=format,
            ),
        })


class AeronaveDetailView(RetrieveAPIView):
    serializer_class = AeronaveDetailSerializer
    queryset = Aeronave.objects.all()
    lookup_field = 'matricula'
    lookup_url_kwarg = 'matricula'
