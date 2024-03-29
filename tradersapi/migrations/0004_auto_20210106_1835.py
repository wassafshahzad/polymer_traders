# Generated by Django 3.1.4 on 2021-01-06 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tradersapi', '0003_chemicalmodel'),
    ]

    def populate_chemical_model(apps, schema_editor):
        ChemicalModel = apps.get_model("tradersapi", "ChemicalModel")
        ChemicalModel.objects.bulk_create([
            ChemicalModel(chemical_name="PP"),
            ChemicalModel(chemical_name="HDPE"),
            ChemicalModel(chemical_name="LDPF"),
            ChemicalModel(chemical_name="LLDPE"),
            ChemicalModel(chemical_name="PVC"),
            ChemicalModel(chemical_name="PS"),
            ChemicalModel(chemical_name="ABS"),
            ChemicalModel(chemical_name="PET"),
            ChemicalModel(chemical_name="EVA"),
            ChemicalModel(chemical_name="PC")
        ])

    operations = [
        migrations.RunPython(populate_chemical_model)
    ]
