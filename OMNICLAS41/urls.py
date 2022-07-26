from django.urls import path
from OMNICLAS41.views import *

app_name = 'omniclas41'
urlpatterns = [
    path('ListarOMC41/', ListarOmniclass41.as_view(), name='ListarOMC41'),
    path('CrearOMC41/', CrearOmniclass41.as_view(), name='CrearOMC41'),
    path('EditarOMC41/<pk>/', EditarOmniclass41.as_view(), name='EditarOMC41'),
    path('EliminarOMC41/<pk>/', EliminarOmniclass41.as_view(), name='EliminarOMC41'),

    path ('ListarOMC41Nivel1/', ListarOMC41Nivel1.as_view(), name = 'ListarOMC41Nivel1'),
    path('CrearOMC41Nivel1/', CrearOMC41Nivel1.as_view(), name = 'CrearOMC41Nivel1'),
    path('EditarOMC41Nivel1/<pk>/', EditarOMC41Nivel1.as_view(), name ='EditarOMC41Nivel1'),
    path('EliminarOMC41Nivel1/<pk>/', EliminarOMC41Nivel1.as_view(), name = 'EliminarOM41Nivel1'),

    path ('ListarOMC41Nivel2/', ListarOMC41Nivel2.as_view(), name = 'ListarOMC41Nivel2'),
    path('CrearOMC41Nivel2/', CrearOMC41Nivel2.as_view(), name = 'CrearOMC41Nivel2'),
    path('EditarOMC41Nivel2/<pk>/', EditarOMC41Nivel2.as_view(), name ='EditarOMC41Nivel2'),
    path('EliminarOMC41Nivel2/<pk>/', EliminarOMC41Nivel2.as_view(), name = 'EliminarOM41Nivel2'),

    path ('ListarOMC41Nivel3/', ListarOMC41Nivel3.as_view(), name = 'ListarOMC41Nivel3'),
    path('CrearOMC41Nivel3/', CrearOMC41Nivel3.as_view(), name = 'CrearOMC41Nivel3'),
    path('EditarOMC41Nivel3/<pk>/', EditarOMC41Nivel3.as_view(), name ='EditarOMC41Nivel3'),
    path('EliminarOMC41Nivel3/<pk>/', EliminarOMC41Nivel3.as_view(), name = 'EliminarOM41Nivel3'),

    path ('ListarOMC41Nivel4/', ListarOMC41Nivel4.as_view(), name = 'ListarOMC41Nivel4'),
    path('CrearOMC41Nivel4/', CrearOMC41Nivel4.as_view(), name = 'CrearOMC41Nivel4'),
    path('EditarOMC41Nivel4/<pk>/', EditarOMC41Nivel4.as_view(), name ='EditarOMC41Nivel4'),
    path('EliminarOMC41Nivel4/<pk>/', EliminarOMC41Nivel4.as_view(), name = 'EliminarOM41Nivel4'),

    path ('ListarOMC41Nivel5/', ListarOMC41Nivel5.as_view(), name = 'ListarOMC41Nivel5'),
    path('CrearOMC41Nivel5/', CrearOMC41Nivel5.as_view(), name = 'CrearOMC41Nivel5'),
    path('EditarOMC41Nivel5/<pk>/', EditarOMC41Nivel5.as_view(), name ='EditarOMC41Nivel5'),
    path('EliminarOMC41Nivel5/<pk>/', EliminarOMC41Nivel5.as_view(), name = 'EliminarOM41Nivel5'),

    path ('ListarOMC41Nivel6/', ListarOMC41Nivel6.as_view(), name = 'ListarOMC41Nivel6'),
    path('CrearOMC41Nivel6/', CrearOMC41Nivel6.as_view(), name = 'CrearOMC41Nivel6'),
    path('EditarOMC41Nivel6/<pk>/', EditarOMC41Nivel6.as_view(), name ='EditarOMC41Nivel6'),
    path('EliminarOMC41Nivel6/<pk>/', EliminarOMC41Nivel6.as_view(), name = 'EliminarOM41Nivel6'),
]