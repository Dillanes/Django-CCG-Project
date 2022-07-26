from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from usuarios.authentication_mixins import Authentication
from OMNICLAS34.serializers import *





class OMC34Nivel1Relation(Authentication,viewsets.ModelViewSet):
    serializer_class = OMC34Nivel1RelationSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idOmc34N1 = pk).first()
    # def list(self, request):
    #     serializer = self.get_serializer(self.get_queryset(), many=True)
    #     return Response(serializer.data, status = status.HTTP_200_OK)
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe un Registro con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        registro = self.get_queryset().filter(idOmc34N1=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un Registro con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)
 


# Create your views here.
class OMC34Nivel1(Authentication,viewsets.ModelViewSet):
    serializer_class = OMC34Nivel1Serializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idOmc34N1 = pk).first()

    # def list(self, request):
    #     serializer = self.get_serializer(self.get_queryset(), many=True)
    #     return Response(serializer.data, status = status.HTTP_200_OK)
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe un Registro con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        registro = self.get_queryset().filter(idOmc34N1=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un Registro con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)

# TABLA OMNICLAS 34 Nivel 2
class OMC34Nivel2(Authentication,viewsets.ModelViewSet):
    serializer_class = OMC34Nivel2Serializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idOmc34N2 = pk).first()

    # def list(self, request):
    #     serializer = self.get_serializer(self.get_queryset(), many=True)
    #     return Response(serializer.data, status = status.HTTP_200_OK)
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe un Registro con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        registro = self.get_queryset().filter(idOmc34N2=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un Registro con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)

# TABLA OMNICLAS 34 Nivel 3
class OMC34Nivel3(Authentication,viewsets.ModelViewSet):
    serializer_class = OMC34Nivel3Serializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idOmc34N3 = pk).first()

    # def list(self, request):
    #     serializer = self.get_serializer(self.get_queryset(), many=True)
    #     return Response(serializer.data, status = status.HTTP_200_OK)
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe un Registro con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        registro = self.get_queryset().filter(idOmc34N3=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un Registro con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)

# TABLA OMNICLAS 34 Nivel 4
class OMC34Nivel4(Authentication,viewsets.ModelViewSet):
    serializer_class = OMC34Nivel4Serializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idOmc34N4 = pk).first()

    # def list(self, request):
    #     serializer = self.get_serializer(self.get_queryset(), many=True)
    #     return Response(serializer.data, status = status.HTTP_200_OK)
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe un Registro con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        registro = self.get_queryset().filter(idOmc34N4=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un Registro con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)