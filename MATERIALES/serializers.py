from dataclasses import fields
from django.contrib.auth.models import User, Group
from rest_framework import serializers 
from MATERIALES.models import *

#SERIALIZERS PARA EL OMNICLAS 23

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'url', 'email','groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name', 'url']
        
#SERIALIZERS CORRESPONDIENTES A ENTIDADES RELACIONADAS A MATERIALES

class MaterialesSerializer(serializers.ModelSerializer):  #ESTE ME DEBERIA SERVIR PARA GENERAR EL CONSECUTIVO
    class Meta:
        model = Materiales
        fields = '__all__'

class ConcretoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concreto
        fields = '__all__'

class CaracEspeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaracEspe
        fields = '__all__'

class EsfuerzoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Esfuerzo
        fields = '__all__'

class ValorEsfuerzoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValorEsfuerzo
        fields = '__all__'

class TipoResistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoResistencia
        fields = '__all__'

class AplPrincipalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AplPrincipales
        fields = '__all__'

class TMASerializer(serializers.ModelSerializer):
    class Meta:
        model = TMA
        fields = '__all__'

class RevenimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revenimiento
        fields = '__all__'

class DensidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Densidad
        fields = '__all__'

class SistColocacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SistColocacion
        fields = '__all__'

class ClasExposicionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClasExposicion
        fields = '__all__'

class FlujoRevSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlujoRev
        fields = '__all__'

class IonCloruroSerializer(serializers.ModelSerializer):
    class Meta:
        model = IonCloruro
        fields = '__all__'

class FibraConcreSerializer(serializers.ModelSerializer):
    class Meta:
        model = FibraConcre
        fields = '__all__'

class UnidadesMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadesMedida
        fields = '__all__'
