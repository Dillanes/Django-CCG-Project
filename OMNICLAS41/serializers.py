from rest_framework import serializers
from OMNICLAS41.models import *

class OmniClass41Serializer(serializers.ModelSerializer):
    class Meta:
        model = OmniClass41
        fields = '__all__'

class OMC41Nivel1Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC41Nivel1
        fields = '__all__'

class OMC41Nivel2Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC41Nivel2
        fields = '__all__'

class OMC41Nivel3Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC41Nivel3
        fields = '__all__'

class OMC41Nivel4Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC41Nivel4
        fields = '__all__'

class OMC41Nivel5Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC41Nivel5
        fields = '__all__'

class OMC41Nivel6Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC41Nivel6
        fields = '__all__'