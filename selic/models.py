from django.db import models


class Selic(models.Model):
    ano_mes = models.PositiveIntegerField()
    mes = models.PositiveSmallIntegerField()
    ano = models.PositiveSmallIntegerField()
    valor = models.FloatField()

    def __str__(self):
        return str(self.mes) + '/' + str(self.ano) + ' = ' + str(self.valor) + "%"
