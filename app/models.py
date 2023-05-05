from django.db import models

# Create your models here.
class Acoes(models.Model):
    codigo = models.IntegerField()
    descricao = models.CharField(max_length=200)
    data = models.DateField()
    open = models.FloatField()
    close = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    volume = models.IntegerField()

    def __str__(self):
        return self.descricao