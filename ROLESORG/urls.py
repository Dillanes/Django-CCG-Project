from rest_framework.routers import DefaultRouter
from ROLESORG.views import *

router = DefaultRouter()

router.register('RolesOrg', RolesOrg, basename = 'RolesOrg')


urlpatterns = router.urls