from django.contrib import admin
from .models import UserProfileModel, ChemicalModel, ChemicalTypeModel


admin.site.register(UserProfileModel)
admin.site.register(ChemicalTypeModel)
admin.site.register(ChemicalModel)
