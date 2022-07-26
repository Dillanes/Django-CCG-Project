from django.shortcuts import render
from .serializers import *
from .models import *
from usuarios.authentication_mixins import Authentication
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
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

#CRUD DEL NIVEL 1 DE UNIFORMAT
class ListarUFTCategorias(Authentication,ListAPIView):
    serializer_class = UFTCategoriaSerializer
    queryset = UFTCategorias.objects.all()

class CrearCategoria(Authentication,CreateAPIView):
    serializer_class = UFTCategoriaSerializer
    #queryset = UFTCategorias.objects.all()

class EditarCategoria(Authentication,RetrieveUpdateAPIView):
    serializer_class = UFTCategoriaSerializer
    queryset = UFTCategorias.objects.all()

class EliminarCatgoria(Authentication,DestroyAPIView): #para eliminar no es requerido enviar todo el json, sino con el puro id (llave primaria)
    serializer_class = UFTCategoriaSerializer
    # queryset = UFTCategorias.objects.all()
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
    
    def delete(self,request,pk=None):
        registro = self.get_queryset().filter(idUftCat=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'},status.HTTP_200_OK)
        return Response({'error': 'No existe un registro con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)

#CRUD DEL NIVEL 2 DE UNIFORMAT
class ListarUFTNivel2(Authentication,ListAPIView):
    serializer_class = UFTNivel2Serializer
    queryset = UFTNivel2.objects.all()

class CrearUFTNivel2(Authentication,CreateAPIView):
    serializer_class = UFTNivel2Serializer
    # queryset = UFTNivel2.objects.all()

class EditarUFTNivel2(Authentication,RetrieveUpdateAPIView):
    serializer_class = UFTNivel2Serializer
    queryset = UFTNivel2.objects.all()

class EliminarUFTNivel2(Authentication,DestroyAPIView): #para eliminar no es requerido enviar todo el json, sino con el puro id (llave primaria)
    serializer_class = UFTNivel2Serializer
    # queryset = UFTNivel2.objects.all()
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
    
    def delete(self,request,pk=None):
        registro = self.get_queryset().filter(idUftN2=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'},status.HTTP_200_OK)
        return Response({'error': 'No existe un registro con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)

#CRUD DEL NIVEL 3 DE UNIFORMAT
class ListarUFTNivel3(Authentication,ListAPIView):
    serializer_class = UFTNivel3Serializer
    queryset = UFTNivel3.objects.all()

class CrearUFTNivel3(Authentication,CreateAPIView):
    serializer_class = UFTNivel3Serializer
    # queryset = UFTNivel3.objects.all()

class EditarUFTNivel3(Authentication,RetrieveUpdateAPIView):
    serializer_class = UFTNivel3Serializer
    queryset = UFTNivel3.objects.all()

class EliminarUFTNivel3(Authentication,DestroyAPIView): #para eliminar no es requerido enviar todo el json, sino con el puro id (llave primaria)
    serializer_class = UFTNivel3Serializer
    #queryset = UFTNivel3.objects.all()
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
    
    def delete(self,request,pk=None):
        registro = self.get_queryset().filter(idUftN3=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'},status.HTTP_200_OK)
        return Response({'error': 'No existe un registro con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)

#CRUD DEL NIVEL 4 DE UNIFORMAT
class ListarUFTNivel4(Authentication,ListAPIView):
    serializer_class = UFTNivel4Serializer
    queryset = UFTNivel4.objects.all()

class CrearUFTNivel4(Authentication,CreateAPIView):
    serializer_class = UFTNivel4Serializer
    # queryset = UFTNivel4.objects.all()

class EditarUFTNivel4(Authentication,RetrieveUpdateAPIView):
    serializer_class = UFTNivel4Serializer
    queryset = UFTNivel4.objects.all()

class EliminarUFTNivel4(Authentication,DestroyAPIView): #para eliminar no es requerido enviar todo el json, sino con el puro id (llave primaria)
    serializer_class = UFTNivel4Serializer
    # queryset = UFTNivel4.objects.all()
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
    
    def delete(self,request,pk=None):
        registro = self.get_queryset().filter(idUftN4=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'},status.HTTP_200_OK)
        return Response({'error': 'No existe un registro con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)

#CRUD DEL NIVEL 5 DE UNIFORMAT
class ListarUFTNivel5(Authentication,ListAPIView):
    serializer_class = UFTNivel5Serializer
    queryset = UFTNivel5.objects.all()

class CrearUFTNivel5(Authentication,CreateAPIView):
    serializer_class = UFTNivel5Serializer
    # queryset = UFTNivel5.objects.all()

class EditarUFTNivel5(Authentication,RetrieveUpdateAPIView):
    serializer_class = UFTNivel5Serializer
    queryset = UFTNivel5.objects.all()

class EliminarUFTNivel5(Authentication,DestroyAPIView): #para eliminar no es requerido enviar todo el json, sino con el puro id (llave primaria)
    serializer_class = UFTNivel5Serializer
    # queryset = UFTNivel5.objects.all()
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
    
    def delete(self,request,pk=None):
        registro = self.get_queryset().filter(idUftN5=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'},status.HTTP_200_OK)
        return Response({'error': 'No existe un registro con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)