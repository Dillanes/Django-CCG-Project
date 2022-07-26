from django.urls import path, include
from OMNICLAS23.views import *

app_name = 'omniclas23'
urlpatterns = [
    path('ListarOMC23/', ListarOmniclass23.as_view(), name = 'ListarOMC23'),
    path('CrearOMC23/', CrearOmniclass23.as_view(), name = 'CrearOMC23'),
    path('EditarOMC23/<pk>/', EditarOmniclas23.as_view(), name = 'EditarOMC23'),
    path('EliminarOMC23/<pk>/', EliminarOmniclas23.as_view(), name = 'EliminarOMC23'),
    
    path ('ListarOMC23Nivel1/', ListarOMC23Nivel1.as_view(), name = 'ListarOMC23Nivel1'),
    path('CrearOMC23Nivel1/', CrearOMC23Nivel1.as_view(), name = 'CrearOMC23Nivel1'),
    path('EditarOMC23Nivel1/<pk>/', EditarOMC23Nivel1.as_view(), name ='EditarOMC23Nivel1'),
    path('EliminarOMC23Nivel1/<pk>/', EliminarOMC23Nivel1.as_view(), name = 'EliminarOM23Nivel1'),

    path('ListarOMC23Nivel2/', ListarOMC23Nivel2.as_view(), name = 'ListarOMC23Nivel2' ),
    path('CrearOMC23Nivel2/', CrearOMC23Nivel2.as_view(), name = 'CrearOMC23Nivel2'),
    path('EditarOMC23Nivel2/<pk>/', EditarOMC23Nivel2.as_view(), name = 'EditarOMC23Nivel2'),
    path('EliminarOMC23Nivel2/<pk>/', EliminarOMC23Nivel2.as_view(), name = 'EliminarOMC23Nivel2'),

    path('ListarOMC23Nivel3/', ListarOMC23Nivel3.as_view(), name = 'ListarOMC23Nivel3'),
    path('CrearOMC23Nivel3/', CrearOMC23Nivel3.as_view(), name = 'CrearOMC23Nivel3'),
    path('EditarOMC23Nivel3/<pk>/', EditarOMC23Nivel3.as_view(), name = 'EditarOMC23Nivel3'),
    path('EliminarOMC23Nivel3/<pk>/', EliminarOMC23Nivel3.as_view(), name = 'EliminarOMC23Nivel3'),

    path('ListarOMC23Nivel4/', ListarOMC23Nivel4.as_view(), name = 'ListarOMC23Nivel4'),
    path('CrearOMC23Nivel4/', CrearOMC23Nivel4.as_view(), name = 'CrearOMC23Nivel4'),
    path('EditarOMC23Nivel4/<pk>/', EditarOMC23Nivel4.as_view(), name = 'EditarOMC23Nivel4'),
    path('EliminarOMC23Nivel4/<pk>/', EliminarOMC23Nivel4.as_view(), name = 'EliminarOMC23Nivel4'),

    path('ListarOMC23Nivel5/', ListarOMC23Nivel5.as_view(), name = 'ListarOMC23Nivel5'),
    path('CrearOMC23Nivel5/', CrearOMC23Nivel5.as_view(), name = 'CrearOMC23Nivel5'),
    path('EditarOMC23Nivel5/<pk>/', EditarOMC23Nivel5.as_view(), name = 'EditarOMC23Nivel5'),
    path('EliminarOMC23Nivel5/<pk>/', EliminarOMC23Nivel5.as_view(), name = 'EliminarOMC23Nivel5'),

    path('ListarOMC23Nivel6/', ListarOMC23Nivel6.as_view(), name = 'ListarOMC23Nivel6'),
    path('CrearOMC23Nivel6/', CrearOMC23Nivel6.as_view(), name = 'CrearOMC23Nivel6'),
    path('EditarOMC23Nivel6/<pk>/', EditarOMC23Nivel6.as_view(), name = 'EditarOMC23Nivel6'),
    path('EliminarOMC23Nivel6/<pk>/', EliminarOMC23Nivel6.as_view(), name = 'EliminarOMC23Nivel6'),
]
