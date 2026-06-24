from rest_framework import serializers


class MatriculaSerializer(serializers.Serializer):
    matricula = serializers.CharField()
    fabricante = serializers.CharField(allow_null=True)
