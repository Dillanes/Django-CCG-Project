from django.urls import path
from UNIFORMAT.views import * 


#app_name = 'uniformat'
urlpatterns=[
    #NIVEL 1
    path('ListaUFTN1/',ListarUFTCategorias.as_view(), name='ListarUFTN1'),
    path('CreaUFTN1/',CrearCategoria.as_view(), name='CrearUFTN1'),
    path('EditaUFTN1/<pk>/',EditarCategoria.as_view(), name='EditarUFTN1'),
    path('EliminaUFTN1/<pk>/',EliminarCatgoria.as_view(), name='EliminarUFTN1'),
    #NIVEL 2
    path('ListaUFTN2/',ListarUFTNivel2.as_view(), name='ListarUFTN2'),
    path('CreaUFTN2/',CrearUFTNivel2.as_view(), name='CrearUFTN2'),
    path('EditaUFTN2/<pk>/',EditarUFTNivel2.as_view(), name='EditarUFTN2'),
    path('EliminaUFTN2/<pk>/',EliminarUFTNivel2.as_view(), name='EliminarUFTNivel2'),
    #NIVEL 3
    path('ListaUFTN3/',ListarUFTNivel3.as_view(), name='ListarUFTN3'),
    path('CreaUFTN3/',CrearUFTNivel3.as_view(), name='CrearUFTN3'),
    path('EditaUFTN3/<pk>/',EditarUFTNivel3.as_view(), name='EditarUFTN3'),
    path('EliminaUFTN3/<pk>/',EliminarUFTNivel3.as_view(), name='EliminarUFTNivel3'),
    #NIVEL 4
    path('ListaUFTN4/',ListarUFTNivel4.as_view(), name='ListarUFTN4'),
    path('CreaUFTN4/',CrearUFTNivel4.as_view(), name='CrearUFTN4'),
    path('EditaUFTN4/<pk>/',EditarUFTNivel4.as_view(), name='EditarUFTN4'),
    path('EliminaUFTN4/<pk>/',EliminarUFTNivel4.as_view(), name='EliminarUFTNivel4'),
    #NIVEL 5
    path('ListaUFTN5/',ListarUFTNivel5.as_view(), name='ListarUFTN5'),
    path('CreaUFTN5/',CrearUFTNivel5.as_view(), name='CrearUFTN5'),
    path('EditaUFTN5/<pk>/',EditarUFTNivel5.as_view(), name='EditarUFTN5'),
    path('EliminaUFTN5/<pk>/',EliminarUFTNivel5.as_view(), name='EliminarUFTNivel5'),
]