from django.contrib import admin

from tradersapi.services.user_service.models import ImageModel
from .models import UserProfileModel, ChemicalModel, ChemicalTypeModel, UserPost


admin.site.register(UserProfileModel)
admin.site.register(ChemicalTypeModel)
admin.site.register(ChemicalModel)
admin.site.register(UserPost)
admin.site.register(ImageModel)