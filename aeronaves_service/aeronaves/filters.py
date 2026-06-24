import unicodedata

import django_filters

from .models import Aeronave


def _normalize(value):
    return (
        "".join(
            c
            for c in unicodedata.normalize("NFKD", value or "")
            if not unicodedata.combining(c)
        )
        .strip()
        .upper()
    )


class AeronaveFilter(django_filters.FilterSet):
    tipoVeiculo = django_filters.CharFilter(
        method="filter_tipo_veiculo", label="Tipo de Veículo"
    )
    search = django_filters.CharFilter(method="filter_search", label="Busca")

    class Meta:
        model = Aeronave
        fields = ["tipoVeiculo", "search"]

    def filter_tipo_veiculo(self, queryset, name, value):
        alvo = _normalize(value)
        variantes = [
            v
            for v in Aeronave.objects.values_list("tipo_veiculo", flat=True).distinct()
            if v and _normalize(v) == alvo
        ]
        return queryset.filter(tipo_veiculo__in=variantes)

    def filter_search(self, queryset, name, value):
        alvo = _normalize(value)
        return queryset.filter(matricula__icontains=alvo)
