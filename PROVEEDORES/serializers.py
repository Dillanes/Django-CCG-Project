from dataclasses import fields
from rest_framework import serializers
from PROVEEDORES.models import *

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'

class SectorMercadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectorMercado
        fields = '__all__'

class ProveedorMarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProveedorMarca
        fields = '__all__'

class SucursalProvSerializer(serializers.ModelSerializer):
    class Meta:
        model = SucursalProv
        fields = '__all__'

class SectorProvSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectorProv
        fields = '__all__'
