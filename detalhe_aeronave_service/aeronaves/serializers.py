from rest_framework import serializers

from .models import Aeronave


class AeronaveDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aeronave
        fields = [
            'matricula',
            'fabricante',
            'tipo_veiculo',
            'houve_ocorrencia',
            'passageiros_maximos',
            'proprietario',
        ]
