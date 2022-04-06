from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers


class CreatableSlugField(serializers.SlugRelatedField):
    def to_internal_value(self, data):
        try:
            return self.get_queryset().get_or_create(**{self.slug_field: data})[0]
        except ObjectDoesNotExist:
            self.fail(
                "does_not_exist", slug_name=self.slug_field, value=str(data)
            )
        except (TypeError, ValueError):
            self.fail("invalid")
