# Generated by Django 3.1.4 on 2021-02-26 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tradersapi', '0008_auto_20210127_1856'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofilemodel',
            options={'verbose_name': 'UserProfileModel', 'verbose_name_plural': 'User Profiles'},
        ),
        migrations.CreateModel(
            name='UserProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.CharField(max_length=255)),
                ('price_per_bad', models.FloatField()),
                ('chemical', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chemical_product', to='tradersapi.chemicalmodel')),
                ('chemical_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tradersapi.chemicaltypemodel')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='tradersapi.userprofilemodel')),
            ],
        ),
    ]
