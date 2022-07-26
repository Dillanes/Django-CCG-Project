from django.urls import path, include
from rest_framework.routers import DefaultRouter
from OMNICLAS34.views import *

router = DefaultRouter()


router.register('OMC34Nivel1Relation', OMC34Nivel1Relation, basename = 'OMC34Nivel1Relation')
router.register('OMC34Nivel1', OMC34Nivel1, basename = 'OMC34Nivel1')
router.register('OMC34Nivel2', OMC34Nivel2, basename = 'OMC34Nivel2')
router.register('OMC34Nivel3', OMC34Nivel3, basename = 'OMC34Nivel3')
router.register('OMC34Nivel4', OMC34Nivel4, basename = 'OMC34Nivel4')

urlpatterns = router.urls

# urlpatterns = [
#     path('', include(router.urls)),
# ]