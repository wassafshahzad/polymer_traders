
from django.db import models


class ChemicalTypeModel(models.Model):

    chem_type = models.CharField(max_length=255)

    class Meta:
        verbose_name = ("type")
        verbose_name_plural = ("chemical type")

    def __str__(self):
        return self.chem_type
