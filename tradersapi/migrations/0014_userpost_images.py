# Generated by Django 3.1.4 on 2022-03-15 18:30

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradersapi', '0013_userpost_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpost',
            name='images',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.ImageField(blank=True, null=True, upload_to='upload/'), default=None, size=None),
            preserve_default=False,
        ),
    ]
