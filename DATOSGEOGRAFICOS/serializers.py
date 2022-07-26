from rest_framework import serializers
from DATOSGEOGRAFICOS.models import *

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = '__all__'

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mundeleg
        fields = '__all__'

class CPSerializer(serializers.ModelSerializer):
    class Meta:
        model = CP
        fields = '__all__'