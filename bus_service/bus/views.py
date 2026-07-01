import requests
from django.conf import settings
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

TIMEOUT = 10

# Cabeçalhos que não devem ser repassados do upstream para o cliente: são
# negociados por conexão (hop-by-hop) e o servidor WSGI os recalcula.
_HOP_BY_HOP = {"content-encoding", "content-length", "transfer-encoding", "connection"}


def _proxy(request, url):
    """Encaminha a requisição GET para o `url` upstream e devolve a resposta."""
    upstream = requests.get(url, params=request.GET, timeout=TIMEOUT)
    response = HttpResponse(
        upstream.content,
        status=upstream.status_code,
        content_type=upstream.headers.get("Content-Type"),
    )
    for key, value in upstream.headers.items():
        if key.lower() not in _HOP_BY_HOP and key.lower() != "content-type":
            response[key] = value
    return response


class ApiRootView(APIView):
    """Lista os endpoints disponíveis no BUS."""

    def get(self, request, format=None):
        return Response(
            {
                "aeronaves": reverse("aeronaves", request=request, format=format),
                "filtros": reverse("filtros", request=request, format=format),
                "detalhe": request.build_absolute_uri("/aeronaves/<matricula>/"),
            }
        )


class MatriculasView(APIView):
    def get(self, request):
        return _proxy(request, f"{settings.AERONAVES_SERVICE_URL}/matriculas")


class FiltrosView(APIView):
    def get(self, request):
        return _proxy(request, f"{settings.AERONAVES_SERVICE_URL}/filtros")


class DetalheAeronaveView(APIView):
    def get(self, request, matricula):
        return _proxy(
            request, f"{settings.DETALHE_SERVICE_URL}/aeronaves/{matricula}/"
        )
