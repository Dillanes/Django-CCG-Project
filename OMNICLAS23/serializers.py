from rest_framework import serializers, pagination
from .models import *

class Omniclass23Serializer(serializers.ModelSerializer):
    class Meta:
        model = OmniClass23
        fields = '__all__'

class OMC23Nivel1Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC23Nivel1
        fields = '__all__'

class OMC23Nivel2Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC23Nivel2
        fields = '__all__'

class OMC23Nivel3Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC23Nivel3
        fields = '__all__'

class OMC23Nivel4Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC23Nivel4
        fields = '__all__'

class OMC23Nivel5Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC23Nivel5
        fields = '__all__'

class OMC23Nivel6Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC23Nivel6
        fields = '__all__'