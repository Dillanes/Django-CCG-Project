from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from usuarios.authentication_mixins import Authentication
from DATOSGEOGRAFICOS.models import *
from DATOSGEOGRAFICOS.serializers import *

# Create your views here.
class VistaCP(Authentication,viewsets.ModelViewSet):
    serializer_class = CPSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(cp = pk).first()

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe un CP con esos datos'}, status = status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        registro = self.get_queryset().filter(cp=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'CP eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un CP con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)

class VistaMunDeleg(Authentication,viewsets.ModelViewSet):
    serializer_class = MunicipioSerializer
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idMunDeleg = pk).first()
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe un Municipio/Delegación con esos datos'}, status = status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        registro = self.get_queryset().filter(idMunDeleg=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Municipio/Delegación eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un Municipio/Delegación con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)

class VistaEstado(Authentication,viewsets.ModelViewSet):
    serializer_class = EstadoSerializer
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idEstado = pk).first()
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe un Estado con esos datos'}, status = status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        registro = self.get_queryset().filter(idEstado=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Estado eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un Estado con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)

class VistaPais(Authentication,viewsets.ModelViewSet):
    serializer_class = PaisSerializer
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idPais = pk).first()

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe un País con esos datos'}, status = status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        registro = self.get_queryset().filter(idPais=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'País eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un País con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)