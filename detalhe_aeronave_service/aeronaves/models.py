from django.db import models


class Aeronave(models.Model):
    matricula = models.CharField(max_length=16, primary_key=True)
    fabricante = models.CharField(max_length=128, null=True, blank=True)
    tipo_veiculo = models.CharField(max_length=64, null=True, blank=True)
    houve_ocorrencia = models.BooleanField(null=True)
    passageiros_maximos = models.IntegerField(null=True, blank=True)
    proprietario = models.CharField(max_length=256, null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'aeronaves'
