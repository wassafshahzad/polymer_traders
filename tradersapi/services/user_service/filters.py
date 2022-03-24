from django_filters import rest_framework as filters
from .models import UserPost

class UserPostFilter(filters.FilterSet):

    chemical = filters.CharFilter(
        field_name="chemical__chemical_name",
        lookup_expr="exact")
    
    chemical_type = filters.CharFilter(
        field_name="chemical_type__chem_type",
        lookup_expr="exact")

    class Meta:
        model = UserPost
        fields = ["created_by", "post_type", "chemical", "chemical_type"]