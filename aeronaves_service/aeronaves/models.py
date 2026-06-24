from django.db import models


class Aeronave(models.Model):
    matricula = models.CharField(max_length=16, primary_key=True)
    fabricante = models.CharField(max_length=128, null=True, blank=True)
    tipo_veiculo = models.CharField(max_length=64, null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'aeronaves'
