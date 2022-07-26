from rest_framework.routers import DefaultRouter
from OMNICLAS35.views import *

router = DefaultRouter()

router.register('OMC35Nivel1', OMC35Nivel1, basename = 'OMC35Nivel1')
router.register('OMC35Nivel2', OMC35Nivel2, basename = 'OMC35Nivel2')
router.register('OMC35Nivel3', OMC35Nivel3, basename = 'OMC35Nivel3')
router.register('OMC35Nivel4', OMC35Nivel4, basename = 'OMC35Nivel4')
router.register('OMC35Nivel5', OMC35Nivel5, basename = 'OMC35Nivel5')
router.register('OMC35Nivel6', OMC35Nivel6, basename = 'OMC35Nivel6')

urlpatterns = router.urls