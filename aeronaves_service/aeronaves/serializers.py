from rest_framework import serializers


class MatriculaSerializer(serializers.Serializer):
    matricula = serializers.CharField()
    fabricante = serializers.CharField(allow_null=True)


class TipoVeiculoListSerializer(serializers.ListSerializer):
    child = serializers.Serializer()

    def to_representation(self, data):
        return [
            self.child.to_representation((index, tipo))
            for index, tipo in enumerate(data)
        ]


class TipoVeiculoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    value = serializers.CharField()
    label = serializers.CharField()

    class Meta:
        list_serializer_class = TipoVeiculoListSerializer

    def to_representation(self, instance: tuple):
        index, tipo = instance
        return {
            "id": index + 1,
            "value": tipo,
            "label": tipo.capitalize(),
        }
