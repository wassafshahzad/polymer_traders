
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


class ChemicalProduct(models.Model):
    chemical = models.ForeignKey(
        "ChemicalModel", verbose_name="chemicals", on_delete=models.CASCADE, related_name='chemicals')
    chemical_type = models.ForeignKey(
        "ChemicalTypeModel", verbose_name="chemicals_type", on_delete=models.CASCADE, related_name='types')
    quantity = models.CharField(max_length=255, default='')
    price = models.IntegerField(default=0)
