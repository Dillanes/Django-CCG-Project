from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from usuarios.views import *

router = DefaultRouter()
router.register('Empleados', VistaEmpleado, basename = 'VistaEmpleado')
router.register('DatosLaborales', VistaDatosLaborales, basename = 'VistaDatosLaborales')
router.register('Departamento', VistaDepartamento, basename = 'VistaDepartamento')
router.register('Cargo', VistaCargo, basename = 'VistaCargo')
router.register('Contrato', VistaContrato, basename = 'VistaContrato')
router.register('', UsuarioViewSet, basename='users')


urlpatterns = [
    # path('usuario/',UserAPIView.as_view(), name = 'usuario_api')
    path('',include(router.urls))
    # path('Listar/',VistaUsuario, name = 'ListarUsuario'),
    # path('Crear/',VistaUsuario, name = 'CrearUsuario'),
    # path('Editar/<int:pk>/',VistaUsuarioDetalle, name = 'EditarUsuario'),
    # path('Eliminar/<int:pk>/',VistaUsuarioDetalle, name = 'EliminarUsuario')
]