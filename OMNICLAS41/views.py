from django.shortcuts import render
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView

)
from usuarios.authentication_mixins import Authentication
from OMNICLAS41.models import *
from OMNICLAS41.serializers import *


# Create your views here.

#TABLA OMNICLASS 41

class ListarOmniclass41(Authentication,ListAPIView):
    queryset = OmniClass41.objects.all()
    serializer_class = OmniClass41Serializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CrearOmniclass41(Authentication,CreateAPIView):
    #queryset = OmniClass41.objects.all()
    serializer_class = OmniClass41Serializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EditarOmniclass41(Authentication,UpdateAPIView):
    queryset = OmniClass41.objects.all()
    serializer_class = OmniClass41Serializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EliminarOmniclass41(Authentication,DestroyAPIView):
    #queryset = OmniClass41.objects.all()
    serializer_class = OmniClass41Serializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
    
    def delete(self,request,pk=None):
        registro = self.get_queryset().filter(idOmc41=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'},status.HTTP_200_OK)
        return Response({'error': 'No existe un registro con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)

#TABLA OMNICLASS 41 NIVEL 1

class ListarOMC41Nivel1(Authentication,ListAPIView):
    queryset = OMC41Nivel1.objects.all()
    serializer_class = OMC41Nivel1Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CrearOMC41Nivel1(Authentication,CreateAPIView):
    #queryset = OMC41Nivel1.objects.all()
    serializer_class = OMC41Nivel1Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EditarOMC41Nivel1(Authentication,UpdateAPIView):
    queryset = OMC41Nivel1.objects.all()
    serializer_class = OMC41Nivel1Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EliminarOMC41Nivel1(Authentication,DestroyAPIView):
    #queryset = OMC41Nivel1.objects.all()
    serializer_class = OMC41Nivel1Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
    
    def delete(self,request,pk=None):
        registro = self.get_queryset().filter(idOmc41N1=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'},status.HTTP_200_OK)
        return Response({'error': 'No existe un registro con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)

#TABLA OMNICLASS 41 NIVEL 2

class ListarOMC41Nivel2(Authentication,ListAPIView):
    queryset = OMC41Nivel2.objects.all()
    serializer_class = OMC41Nivel2Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CrearOMC41Nivel2(Authentication,CreateAPIView):
    #queryset = OMC41Nivel2.objects.all()
    serializer_class = OMC41Nivel2Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EditarOMC41Nivel2(Authentication,UpdateAPIView):
    queryset = OMC41Nivel2.objects.all()
    serializer_class = OMC41Nivel2Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EliminarOMC41Nivel2(Authentication,DestroyAPIView):
    #queryset = OMC41Nivel2.objects.all()
    serializer_class = OMC41Nivel2Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
    
    def delete(self,request,pk=None):
        registro = self.get_queryset().filter(idOmc41N2=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'},status.HTTP_200_OK)
        return Response({'error': 'No existe un registro con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)

#TABLA OMNICLASS 41 NIVEL 3

class ListarOMC41Nivel3(Authentication,ListAPIView):
    queryset = OMC41Nivel3.objects.all()
    serializer_class = OMC41Nivel3Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CrearOMC41Nivel3(Authentication,CreateAPIView):
    #queryset = OMC41Nivel3.objects.all()
    serializer_class = OMC41Nivel3Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EditarOMC41Nivel3(Authentication,UpdateAPIView):
    queryset = OMC41Nivel3.objects.all()
    serializer_class = OMC41Nivel3Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EliminarOMC41Nivel3(Authentication,DestroyAPIView):
    #queryset = OMC41Nivel3.objects.all()
    serializer_class = OMC41Nivel3Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
    
    def delete(self,request,pk=None):
        registro = self.get_queryset().filter(idOmc41N3=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'},status.HTTP_200_OK)
        return Response({'error': 'No existe un registro con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)

#TABLA OMNICLASS 41 NIVEL 4

class ListarOMC41Nivel4(Authentication,ListAPIView):
    queryset = OMC41Nivel4.objects.all()
    serializer_class = OMC41Nivel4Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CrearOMC41Nivel4(Authentication,CreateAPIView):
    #queryset = OMC41Nivel4.objects.all()
    serializer_class = OMC41Nivel4Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EditarOMC41Nivel4(Authentication,UpdateAPIView):
    queryset = OMC41Nivel4.objects.all()
    serializer_class = OMC41Nivel4Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EliminarOMC41Nivel4(Authentication,DestroyAPIView):
    #queryset = OMC41Nivel4.objects.all()
    serializer_class = OMC41Nivel4Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
    
    def delete(self,request,pk=None):
        registro = self.get_queryset().filter(idOmc41N4=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'},status.HTTP_200_OK)
        return Response({'error': 'No existe un registro con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)

#TABLA OMNICLASS 41 NIVEL 5

class ListarOMC41Nivel5(Authentication,ListAPIView):
    queryset = OMC41Nivel5.objects.all()
    serializer_class = OMC41Nivel5Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CrearOMC41Nivel5(Authentication,CreateAPIView):
    #queryset = OMC41Nivel5.objects.all()
    serializer_class = OMC41Nivel5Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EditarOMC41Nivel5(Authentication,UpdateAPIView):
    queryset = OMC41Nivel5.objects.all()
    serializer_class = OMC41Nivel5Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EliminarOMC41Nivel5(Authentication,DestroyAPIView):
    #queryset = OMC41Nivel5.objects.all()
    serializer_class = OMC41Nivel5Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
    
    def delete(self,request,pk=None):
        registro = self.get_queryset().filter(idOmc41N5=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'},status.HTTP_200_OK)
        return Response({'error': 'No existe un registro con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)

#TABLA OMNICLASS 41 NIVEL 6

class ListarOMC41Nivel6(Authentication,ListAPIView):
    queryset = OMC41Nivel6.objects.all()
    serializer_class = OMC41Nivel6Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CrearOMC41Nivel6(Authentication,CreateAPIView):
    #queryset = OMC41Nivel6.objects.all()
    serializer_class = OMC41Nivel6Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EditarOMC41Nivel6(Authentication,UpdateAPIView):
    queryset = OMC41Nivel6.objects.all()
    serializer_class = OMC41Nivel6Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EliminarOMC41Nivel6(Authentication,DestroyAPIView):
    #queryset = OMC41Nivel6.objects.all()
    serializer_class = OMC41Nivel6Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
    
    def delete(self,request,pk=None):
        registro = self.get_queryset().filter(idOmc41N6=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'},status.HTTP_200_OK)
        return Response({'error': 'No existe un registro con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)
