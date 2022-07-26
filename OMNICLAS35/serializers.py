from rest_framework import serializers
from OMNICLAS35.models import *

class OMC35Nivel1Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC35Nivel1
        fields = '__all__'

class OMC35Nivel2Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC35Nivel2
        fields = '__all__'

class OMC35Nivel3Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC35Nivel3
        fields = '__all__'

class OMC35Nivel4Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC35Nivel4
        fields = '__all__'

class OMC35Nivel5Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC35Nivel5
        fields = '__all__'

class OMC35Nivel6Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC35Nivel6
        fields = '__all__'