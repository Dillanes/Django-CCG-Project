from rest_framework.routers import DefaultRouter
from DATOSGEOGRAFICOS.views import *

router = DefaultRouter()
router.register('CodigoPostal', VistaCP, basename = 'VistaCP')
router.register('Municipio', VistaMunDeleg, basename = 'VistaMunDeleg')
router.register('Estado', VistaEstado, basename = 'VistaEstado')
router.register('Pais', VistaPais, basename = 'VistaPais')

urlpatterns = router.urls