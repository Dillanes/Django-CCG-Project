# from django.contrib.auth.models import User, Group
from django.db import connection
from usuarios.authentication_mixins import Authentication
from MATERIALES.serializers import *
from MATERIALES.models import *
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
)

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#VISTAS PARA MATERIALES

#vistas que insertan en base de datos
class CrearMaterial(Authentication,CreateAPIView):
    serializer_class = MaterialesSerializer
    queryset = Materiales.objects.all()
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CrearConcreto(Authentication,CreateAPIView):
    serializer_class = ConcretoSerializer
    queryset = Concreto.objects.all()
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CrearCaracEspe(Authentication,CreateAPIView):
    serializer_class = CaracEspeSerializer
    queryset = CaracEspe.objects.all()
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#vistas de solo consulta
class ListarMateriales(Authentication,ListAPIView):
    serializer_class = MaterialesSerializer
    def get_queryset(self):
        return Materiales.objects.all()
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ListarConcreto(Authentication,ListAPIView):
    serializer_class = ConcretoSerializer
    def get_queryset(self):
        return Concreto.objects.all()
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ListarEsfuerzo(Authentication,ListAPIView):
    serializer_class = EsfuerzoSerializer
    queryset = Esfuerzo.objects.all()
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ListarValorEsfuerzo(Authentication,ListAPIView):
    serializer_class = ValorEsfuerzoSerializer
    queryset = ValorEsfuerzo.objects.all()
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ListarTipoResistencia(Authentication,ListAPIView):
    serializer_class = TipoResistenciaSerializer
    queryset = TipoResistencia.objects.all()
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ListarAplPrincipales(Authentication,ListAPIView):
    serializer_class = AplPrincipalesSerializer
    queryset = AplPrincipales.objects.all()
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ListarTMA(Authentication,ListAPIView):
    serializer_class = TMASerializer
    queryset = TMA.objects.all()
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ListarRevenimiento(Authentication,ListAPIView):
    serializer_class = RevenimientoSerializer
    queryset = Revenimiento.objects.all()
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ListarDensidad(Authentication,ListAPIView):
    serializer_class = DensidadSerializer
    queryset = Densidad.objects.all()
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ListarSistColocacion(Authentication,ListAPIView):
    serializer_class = SistColocacionSerializer
    queryset = SistColocacion.objects.all()
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ListarClasExposicion(Authentication,ListAPIView):
    serializer_class = ClasExposicionSerializer
    queryset = ClasExposicion.objects.all()
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ListarFlujoRev(Authentication,ListAPIView):
    serializer_class = FlujoRevSerializer
    queryset = FlujoRev.objects.all()
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ListarIonCloruro(Authentication,ListAPIView):
    serializer_class = IonCloruroSerializer
    queryset = IonCloruro.objects.all()
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ListarFibraConcre(Authentication,ListAPIView):
    serializer_class = FibraConcreSerializer
    queryset = FibraConcre.objects.all()
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ListarUnidadesMedida(Authentication,ListAPIView):
    serializer_class = UnidadesMedidaSerializer
    queryset = UnidadesMedida.objects.all()
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# @api_view(['GET'],)
# def ListarConcretosMateriales(request):
#     if request.method == 'GET':
#         with connection.cursor() as cursor:
#             cursor.execute("SELECT Materiales.numMat,Materiales.codigoOmc AS CodigoOmc23,Materiales.Consecutivo,Materiales.descriCorta,Materiales.descriLarga,Materiales.Comentarios,Materiales.palabrasCve,Materiales.desCorEng,Materiales.desLargEng,Materiales.fuenteInf,Materiales.fecRegInf,Materiales.codigoBimsa, Omc23Nivel3.descriSpa AS Nombre,acroEsf.Sigla AS SiglaEsf,ValorEsfuerzo.Valor AS ValorEsfuerzo,uniVal.Unidad,Esfuerzo.tipoEsfuerzo,TipoResistencia.Tipo AS TipoResistencia,acroTma.Sigla as SiglaTma,TMA.valTma,acroRev.Sigla as SiglaRev, Tma.tmaFrac,Revenimiento.valRev,uniRev.Unidad,TipoConsistencia.Tipo AS TipoCons,CaracEspe.modElast,CaracEspe.Acronimo,CaracEspe.Edad,CaracEspe.absorcionCap,CaracEspe.Acronimo2,CaracEspe.trabaExtend,CaracEspe.Clase,CaracEspe.Color,CaracEspe.Comportamiento,CaracEspe.conAire, CaracEspe.conIonClor,CaracEspe.tiempoPrueba,SistColocacion.tipoSistema FROM Omc23Nivel3 JOIN  Materiales on codigoOmc=Omc23Nivel3.Codigo JOIN Concreto on fk_Material=idMaterial JOIN ValorEsfuerzo on fk_ValEsf=idValEsf JOIN Esfuerzo on Esfuerzo.idEsfuerzo=ValorEsfuerzo.fk_Esfuerzo JOIN UnidadesMedida uniVal on uniVal.idUniMed=ValorEsfuerzo.fk_UniMed JOIN Acronimo acroEsf on Esfuerzo.fk_Acronimo=acroEsf.idAcronimo JOIN TipoResistencia on idTipoResist=fk_TipoResist JOIN TMA on fk_Tma=idTma JOIN Acronimo acroTma on Tma.fk_Acronimo=acroTma.idAcronimo JOIN Revenimiento on fk_Reven=idReven JOIN Acronimo acroRev on Revenimiento.fk_Acronimo=acroRev.idAcronimo JOIN UnidadesMedida uniRev on Revenimiento.fk_UniMed=uniRev.idUniMed JOIN TipoConsistencia on fk_TipoCons=TipoConsistencia.idTipoCons JOIN CaracEspe ON fk_Concreto=idConcreto JOIN SistColocacion on fk_SistColoc=idSistColoc")
#             listarConcreto =dictfetchall(cursor)
#             if listarConcreto:
#                 return Response(listarConcreto, status = status.HTTP_200_OK)
#             else:
#                 return Response({'mensaje':'No existe un Registro!'}, status = status.HTTP_400_BAD_REQUEST)

class ListarConcretosMateriales(Authentication,viewsets.GenericViewSet):
    def get_queryset(self):
         with connection.cursor() as cursor:
            listarConcreto = cursor.execute("SELECT Mat.codigoOmc, Mat.Consecutivo,Mat.descriCorta,Mat.descriLarga,Mat.Comentarios,Mat.palabrasCve,Mat.desCorEng,Mat.desLargEng,Mat.fuenteInf,Mat.fecRegInf,Mat.codigoBimsa,Omc23Nivel3.descriSpa AS Nombre,acroEsf.Sigla, ValorEsfuerzo.Valor AS ValorEsfuerzo,uniVal.Unidad,Esfuerzo.tipoEsfuerzo,TipoResistencia.Tipo AS TipoResistencia,acroTma.Sigla,TMA.valTma,acroRev.Sigla,Tma.tmaFrac,Revenimiento.valRev,uniRev.Unidad,TipoConsistencia.Tipo AS TipoCons, CaracEspe.modElast,CaracEspe.Acronimo,CaracEspe.Edad,CaracEspe.absorcionCap,CaracEspe.Acronimo2,CaracEspe.trabaExtend,CaracEspe.Clase,CaracEspe.Color,CaracEspe.Comportamiento,CaracEspe.conAire,CaracEspe.conIonClor,CaracEspe.tiempoPrueba,SistColocacion.tipoSistema FROM Omc23Nivel3 FULL JOIN  Materiales mat ON mat.codigoOmc=Omc23Nivel3.Codigo FULL JOIN  Concreto ON fk_Material=idMaterial FULL JOIN Revenimiento ON fk_Reven=idReven FULL JOIN Acronimo acroRev ON Revenimiento.fk_Acronimo=acroRev.idAcronimo FULL  JOIN UnidadesMedida uniRev ON Revenimiento.fk_UniMed=uniRev.idUniMed FULL JOIN ValorEsfuerzo ON fk_ValEsf=idValEsf JOIN Esfuerzo ON Esfuerzo.idEsfuerzo=ValorEsfuerzo.fk_Esfuerzo JOIN UnidadesMedida uniVal ON uniVal.idUniMed=ValorEsfuerzo.fk_UniMed FULL JOIN Acronimo acroEsf ON Esfuerzo.fk_Acronimo=acroEsf.idAcronimo FULL JOIN TMA ON fk_Tma=idTma FULL JOIN Acronimo acroTma ON Tma.fk_Acronimo=acroTma.idAcronimo FULL JOIN SistColocacion ON fk_SistColoc=idSistColoc FULL JOIN TipoConsistencia ON Revenimiento.fk_TipoCons=TipoConsistencia.idTipoCons FULL JOIN TipoResistencia ON TipoResistencia.idTipoResist=ValorEsfuerzo.fk_TipoResist FULL JOIN CaracEspe ON fk_Concreto=idConcreto  WHERE codigoOmc is not null")
            listarConcreto =dictfetchall(cursor)
            return listarConcreto
        
    
    def list(self,request):
        data = self.get_queryset()
        if data:
            return Response(data, status = status.HTTP_200_OK)
        else:
            return Response({'mensaje':'No existe un Registro!'}, status = status.HTTP_400_BAD_REQUEST)


def dictfetchall(cursor): 
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]