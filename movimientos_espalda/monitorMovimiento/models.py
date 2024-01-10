from django.db import models

class DatosEspalda(models.Model):
    mean = models.FloatField()
    stdv = models.FloatField()

    def __str__(self):
        return f'Mean: {self.mean}, Stdv: {self.stdv}'
