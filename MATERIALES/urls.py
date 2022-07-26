from django.db import router
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from MATERIALES.views import * 

router = DefaultRouter()
# router.register('users', UserViewSet)
# router.register('groups', GroupViewSet)

#MATERIALES
router.register('ListarConcretosMateriales', ListarConcretosMateriales, basename = 'ListarConcretosMateriales')
# router.register('CrearConcreto/', CrearConcreto)
# router.register('CrearCaracEspe/', CrearCaracEspe)
#router.register('Materiales/', MostrarMateriales)


urlpatterns=[
    path('',include(router.urls)),
    path('CrearMaterial/', CrearMaterial.as_view(), name='CrearMaterial'),
    path('CrearConcreto/', CrearConcreto.as_view(), name='CrearConcreto'),
    path('CrearCaracEspe/', CrearCaracEspe.as_view(), name='CrearCaracEspe'),
    path('ListarEsfuerzo/', ListarEsfuerzo.as_view(), name='ListarEsfuerzo'),
    path('ListarValorEsfuerzo/', ListarValorEsfuerzo.as_view(), name='ListarValorEsfuerzo'),
    path('ListarTipoResistencia/', ListarTipoResistencia.as_view(), name='ListarTipoResistencia'),
    path('ListarAplPrincipales/', ListarAplPrincipales.as_view(), name='ListarAplPrincipales'),
    path('ListarTMA/', ListarTMA.as_view(), name='ListarTMA'),
    path('ListarRevenimiento/', ListarRevenimiento.as_view(), name='ListarRevenimiento'),
    path('ListarDensidad/', ListarDensidad.as_view(), name='ListarDensidad'),
    path('ListarSistColocacion/', ListarSistColocacion.as_view(), name='ListarSistColocacion'),
    path('ListarClasExposicion/', ListarClasExposicion.as_view(), name='ListarClasExposicion'),
    path('ListarFlujoRev/', ListarFlujoRev.as_view(), name='ListarFlujoRev'),
    path('ListarIonCloruro/', ListarIonCloruro.as_view(), name='ListarIonCloruro'),
    path('ListarFibraConcre/', ListarFibraConcre.as_view(), name='ListarFibraConcre'),
    path('ListarUnidadesMedida/', ListarUnidadesMedida.as_view(), name='ListarUnidadesMedida'),
    path('ListarMateriales/', ListarMateriales.as_view(), name='ListarMateriales'),
    path('ListarConcreto/', ListarConcreto.as_view(), name='ListarConcreto'),
    # path('ListarConcretosMateriales/', ListarConcretosMateriales, name='ListarConcretosMateriales'),

]




