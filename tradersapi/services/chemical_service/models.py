
from django.db import models
from django.db.models.fields import CharField


class ChemicalTypeModel(models.Model):

    chem_type = models.CharField(max_length=255)

    class Meta:
        verbose_name = ("type")
        verbose_name_plural = ("chemical type")

    def __str__(self):
        return self.chem_type


class ChemicalModel(models.Model):

    chemical_name = CharField(max_length=255, unique=True)

    def __str__(self):
        return self.chemical_name
