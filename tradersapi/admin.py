from django.contrib import admin
from .models import UserProfileModel, ChemicalModel, ChemicalTypeModel
# Register your models here.


admin.site.register(UserProfileModel)
admin.site.register(ChemicalTypeModel)
admin.site.register(ChemicalModel)
