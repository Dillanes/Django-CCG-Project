from django.shortcuts import render
from .models import *
from .serializers import *
from usuarios.authentication_mixins import Authentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
)

# Create your views here.

#TABLA OMNICLASS 23

class ListarOmniclass23(Authentication,ListAPIView):
    queryset = OmniClass23.objects.all()
    serializer_class = Omniclass23Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CrearOmniclass23(Authentication,CreateAPIView):
    #queryset = OmniClass23.objects.all()
    serializer_class = Omniclass23Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EditarOmniclas23(Authentication,UpdateAPIView):
    queryset = OmniClass23.objects.all()
    serializer_class = Omniclass23Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EliminarOmniclas23(Authentication,DestroyAPIView):
    #queryset = OmniClass23.objects.all()
    serializer_class = Omniclass23Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
    
    def delete(self,request,pk=None):
        registro = self.get_queryset().filter(idOmc23=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'},status.HTTP_200_OK)
        return Response({'error': 'No existe un registro con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)

#TABLA OMNICLASS 23 NIVEL 1

class ListarOMC23Nivel1(Authentication,ListAPIView):
    queryset = OMC23Nivel1.objects.all()
    serializer_class = OMC23Nivel1Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CrearOMC23Nivel1(Authentication,CreateAPIView):
    #queryset = OMC23Nivel1.objects.all()
    serializer_class = OMC23Nivel1Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EditarOMC23Nivel1(Authentication,RetrieveUpdateAPIView):
    queryset = OMC23Nivel1.objects.all()
    serializer_class = OMC23Nivel1Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EliminarOMC23Nivel1(Authentication,DestroyAPIView):
    #queryset = OMC23Nivel1.objects.all()
    serializer_class = OMC23Nivel1Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
    
    def delete(self,request,pk=None):
        registro = self.get_queryset().filter(idOmc23N1=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'},status.HTTP_200_OK)
        return Response({'error': 'No existe un registro con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)

#TABLA OMNICLASS 23 NIVEL 2

class ListarOMC23Nivel2(Authentication,ListAPIView):
    queryset = OMC23Nivel2.objects.all()
    serializer_class = OMC23Nivel2Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CrearOMC23Nivel2(Authentication,CreateAPIView):
    #queryset = OMC23Nivel2.objects.all()
    serializer_class = OMC23Nivel2Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EditarOMC23Nivel2(Authentication,UpdateAPIView):
    queryset = OMC23Nivel2.objects.all()
    serializer_class = OMC23Nivel2Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EliminarOMC23Nivel2(Authentication,DestroyAPIView):
    #queryset = OMC23Nivel2.objects.all()
    serializer_class = OMC23Nivel2Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
    
    def delete(self,request,pk=None):
        registro = self.get_queryset().filter(idOmc23N2=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'},status.HTTP_200_OK)
        return Response({'error': 'No existe un registro con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)

#TABLA OMNICLASS 23 NIVEL 3

class ListarOMC23Nivel3(Authentication,ListAPIView):
    queryset = OMC23Nivel3.objects.all()
    serializer_class = OMC23Nivel3Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CrearOMC23Nivel3(Authentication,CreateAPIView):
    #queryset = OMC23Nivel3.objects.all()
    serializer_class = OMC23Nivel3Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EditarOMC23Nivel3(Authentication,UpdateAPIView):
    queryset = OMC23Nivel3.objects.all()
    serializer_class = OMC23Nivel3Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EliminarOMC23Nivel3(Authentication,DestroyAPIView):
    #queryset = OMC23Nivel3.objects.all()
    serializer_class = OMC23Nivel3Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
    
    def delete(self,request,pk=None):
        registro = self.get_queryset().filter(idOmc23N3=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'},status.HTTP_200_OK)
        return Response({'error': 'No existe un registro con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)

#TABLA OMNICLASS 23 NIVEL 4

class ListarOMC23Nivel4(Authentication,ListAPIView):
    queryset = OMC23Nivel4.objects.all()
    serializer_class = OMC23Nivel4Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CrearOMC23Nivel4(Authentication,CreateAPIView):
    #queryset = OMC23Nivel4.objects.all()
    serializer_class = OMC23Nivel4Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EditarOMC23Nivel4(Authentication,UpdateAPIView):
    queryset = OMC23Nivel4.objects.all()
    serializer_class = OMC23Nivel4Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EliminarOMC23Nivel4(Authentication,DestroyAPIView):
    #queryset = OMC23Nivel4.objects.all()
    serializer_class = OMC23Nivel4Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
    
    def delete(self,request,pk=None):
        registro = self.get_queryset().filter(idOmc23N4=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'},status.HTTP_200_OK)
        return Response({'error': 'No existe un registro con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)

#TABLA OMNICLASS 23 NIVEL 5

class ListarOMC23Nivel5(Authentication,ListAPIView):
    queryset = OMC23Nivel5.objects.all()
    serializer_class = OMC23Nivel5Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CrearOMC23Nivel5(Authentication,CreateAPIView):
    #queryset = OMC23Nivel5.objects.all()
    serializer_class = OMC23Nivel5Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EditarOMC23Nivel5(Authentication,UpdateAPIView):
    queryset = OMC23Nivel5.objects.all()
    serializer_class = OMC23Nivel5Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EliminarOMC23Nivel5(Authentication,DestroyAPIView):
    #queryset = OMC23Nivel5.objects.all()
    serializer_class = OMC23Nivel5Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
    
    def delete(self,request,pk=None):
        registro = self.get_queryset().filter(idOmc23N5=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'},status.HTTP_200_OK)
        return Response({'error': 'No existe un registro con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)

#TABLA OMNICLASS 23 NIVEL 6

class ListarOMC23Nivel6(Authentication,ListAPIView):
    queryset = OMC23Nivel6.objects.all()
    serializer_class = OMC23Nivel6Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CrearOMC23Nivel6(Authentication,CreateAPIView):
    #queryset = OMC23Nivel6.objects.all()
    serializer_class = OMC23Nivel6Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EditarOMC23Nivel6(Authentication,UpdateAPIView):
    queryset = OMC23Nivel6.objects.all()
    serializer_class = OMC23Nivel6Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EliminarOMC23Nivel6(Authentication,DestroyAPIView):
    #queryset = OMC23Nivel6.objects.all()
    serializer_class = OMC23Nivel6Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
    
    def delete(self,request,pk=None):
        registro = self.get_queryset().filter(idOmc23N6=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'},status.HTTP_200_OK)
        return Response({'error': 'No existe un registro con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)

