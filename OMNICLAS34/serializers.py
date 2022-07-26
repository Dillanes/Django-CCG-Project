from rest_framework import serializers
from OMNICLAS34.models import *
from ROLESORG.models import RolesOrg


class OMC34Nivel1Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC34Nivel1
        fields= '__all__'

class OMC34Nivel2Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC34Nivel2
        fields= '__all__'

class OMC34Nivel3Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC34Nivel3
        fields= '__all__'

class OMC34Nivel4Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC34Nivel4
        fields = ('idOmc34N4','Codigo','descriEng','descriSpa','definicionEng','definicionSpa','anioReg','regFinal')
        # fields = '__all__'


class OMC34Nivel3RelationSerializer(serializers.ModelSerializer):
    children = OMC34Nivel4Serializer(many=True)
    class Meta:
        model = OMC34Nivel3
        fields = ('idOmc34N3','Codigo','descriEng','descriSpa','definicionEng','definicionSpa','anioReg','regFinal','children')

class OMC34Nivel2RelationSerializer(serializers.ModelSerializer):
    children = OMC34Nivel3RelationSerializer(many=True)
    class Meta:
        model = OMC34Nivel2
        fields = ('idOmc34N2','Codigo','descriEng','descriSpa','definicionEng','definicionSpa','anioReg','regFinal','children')

class OMC34Nivel1RelationSerializer(serializers.ModelSerializer):
    children = OMC34Nivel2RelationSerializer(many=True)
    class Meta:
        model = OMC34Nivel1
        fields = ('idOmc34N1','Codigo','descriEng','descriSpa','definicionEng','definicionSpa','anioReg','children')



