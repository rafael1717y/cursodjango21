from django.db import models


class Contribuinte(models.Model):
    ni = models.CharField(max_length=14)
    nome = models.CharField(max_length=255)
    contato = models.TextField(blank=True)

    def __str__(self):
        return self.nome
