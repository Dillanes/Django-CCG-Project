from rest_framework import serializers
from ROLESORG.models import *

class RolesOrgSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolesOrg
        fields = '__all__'
