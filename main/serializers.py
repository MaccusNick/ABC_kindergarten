from rest_framework import serializers
from .models import (
    Parent
)


class ParentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Parent
        fields = ('Parentid', 'FirstName', 'LastName', 'PhoneNumber', 'Email')

