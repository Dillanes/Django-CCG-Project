from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from usuarios.authentication_mixins import Authentication
from ROLESORG.serializers import *

# Create your views here.
class RolesOrg(Authentication,viewsets.ModelViewSet):
    serializer_class = RolesOrgSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idRolOrg=pk).first()
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe un Registro con esos datos'}, status = status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        registro = self.get_queryset(pk)
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un Registro con estos datos'}, status = status.HTTP_400_BAD_REQUEST)


