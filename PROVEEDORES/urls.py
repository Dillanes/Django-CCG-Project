from rest_framework.routers import DefaultRouter
from PROVEEDORES.views import *

router = DefaultRouter()
router.register('Proveedor', VistaProveedor, basename = 'VistaProveedor')
router.register('Marca', VistaMarca, basename = 'VistaMarca')
router.register('SectorMercado', VistaSectorMercado, basename = 'VistaSectorMercado')
router.register('ProveedorMarca', VistaProveedorMarca, basename = 'VistaProveedorMarca')
router.register('SucursalProveedor', VistaSucursalProv, basename = 'VistaSucursalProv')
router.register('SectorProveedor', VistaSectorProv, basename = 'VistaSectorProv')
router.register('ListarSectorXProveedor', ListarSectorXProveedor, basename = 'ListarSectorXProveedor')
router.register('ListarMarcaXProveedor', ListarMarcaXProveedor, basename = 'ListarMarcaXProveedor')
router.register('ListarSucursalXProveedor', ListarSucursalXProveedor, basename = 'ListarSucursalXProveedor')

urlpatterns = router.urls